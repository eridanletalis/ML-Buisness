"""Модуль бекэенда прогнозирования"""

from logging.handlers import RotatingFileHandler
from time import strftime, time
import logging
import traceback
import h2o
from flask import Flask, request, jsonify
from addfuncs import processinput


app = Flask(__name__)

h2o.init()
MODEL_GLM_POISSON = h2o.load_model('models/GLM_model_python_1591832595250_1')
MODEL_GLM_GAMMA = h2o.load_model('models/GLM_model_python_1591832595250_2')

# Logging
HANDLER = RotatingFileHandler('backend.log', maxBytes=100000, backupCount=5)
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)
LOGGER.addHandler(HANDLER)


@app.route("/")
def index():
    """Вывод стартовой страницы"""
    return "Welcome to API"


@app.route("/predict", methods=['POST'])
def predict():
    """функция при пост-запросе predict"""
    json_input = request.json

    # Request logging
    current_datatime = strftime('[%Y-%b-%d %H:%M:%S]')
    ip_address = request.headers.get("X-Forwarded-For", request.remote_addr)
    LOGGER.info(
        f'{current_datatime} request from {ip_address}: {request.json}')
    start_prediction = time()

    clientid = json_input['ID']
    frame = processinput(json_input)

    prediction_poisson = MODEL_GLM_POISSON.predict(frame)
    value_poisson = prediction_poisson.as_data_frame()['predict'][0]

    prediction_gamma = MODEL_GLM_GAMMA.predict(frame)
    value_gamma = prediction_gamma.as_data_frame()['predict'][0]

    value_burningcost = value_poisson * value_gamma

    result = {
        'ID': clientid,
        'value_Poisson': value_poisson,
        'value_Gamma': value_gamma,
        'value_BurningCost': value_burningcost
    }

    # Response logging
    end_prediction = time()
    duration = round(end_prediction - start_prediction, 6)
    current_datatime = strftime('[%Y-%b-%d %H:%M:%S]')
    LOGGER.info(
        f'{current_datatime} predicted for {duration} msec: {result}\n')

    return jsonify(result)


@app.errorhandler(Exception)
def exceptions(e):
    """Обработка ошибок"""
    current_datatime = strftime('[%Y-%b-%d %H:%M:%S]')
    error_message = traceback.format_exc()
    LOGGER.error('%s %s %s %s %s 5xx INTERNAL SERVER ERROR\n%s',
                 current_datatime,
                 request.remote_addr,
                 request.method,
                 request.scheme,
                 request.full_path,
                 error_message)
    return jsonify({'error': 'Internal Server Error'}), 500


if __name__ == '__main__':
    app.run(debug=True)
