"""модуль фронт-энд сервиса"""
import json

from flask import Flask, render_template, redirect, url_for, request
from flask_wtf import FlaskForm
from requests.exceptions import ConnectionError
from wtforms import IntegerField, SelectField
from wtforms.validators import DataRequired

from postman import data, send_json


class ClientDataForm(FlaskForm):
    """класс, отвечающий за предопределение текстовых полей веб-страницы"""
    id = IntegerField('ID', validators=[DataRequired()])
    age = IntegerField('Возраст водителя', validators=[DataRequired()])
    lic_age = IntegerField('Водительский стаж', validators=[DataRequired()])
    gender = SelectField('Пол', choices=[('Male', 'М'), ('Female', 'Ж')])
    mari_stat = SelectField(
        'Семейное положение', choices=[
            ('Alone', 'Alone'), ('Other', 'Other')])
    veh_age = IntegerField('Возраст автомобиля', validators=[DataRequired()])
    bonus_malus = IntegerField(
        'Коэффициент BonusMalus',
        validators=[
            DataRequired()])


app = Flask(__name__)
app.config.update(
    CSRF_ENABLED=True,
    SECRET_KEY='you-will-never-guess',
)


@app.route("/")
def index():
    """вывод стартовой страницы"""
    return render_template('index.html')


@app.route('/predicted/<response>')
def predicted(response):
    """вывод результата прогноза"""
    response = json.loads(response)
    print(response)
    return render_template('predicted.html', response=response)


@app.route('/predict_form', methods=['GET', 'POST'])
def predict_form():
    """функция ввода данных"""
    dict_data = data
    form = ClientDataForm()
    if request.method == 'POST':
        dict_data['ID'] = request.form.get('id')
        dict_data['DrivAge'] = float(request.form.get('age'))
        dict_data['LicAge'] = float(request.form.get('lic_age'))
        dict_data['Gender'] = request.form.get('gender')
        dict_data['MariStat'] = request.form.get('mari_stat')
        dict_data['VehAge'] = float(request.form.get('veh_age'))
        dict_data['BonusMalus'] = float(request.form.get('bonus_malus'))
        try:
            response = send_json(dict_data)
            response = response.text
        except ConnectionError:
            response = json.dumps({"error": "ConnectionError"})
        return redirect(url_for('predicted', response=response))
    return render_template('form.html', form=form)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001, debug=True)
