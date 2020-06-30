"""модуль, отвечающий за отправку ПОСТ-запроса на бекэнд"""
import requests

DATA = {
    "ID": 1,
    "LicAge": 468,
    "RecordBeg": "2004-01-01",
    "RecordEnd": "",
    "VehAge": "",
    "Gender": "Male",
    "MariStat": "Other",
    "SocioCateg": "CSP50",
    "VehUsage": "Private",
    "DrivAge": 67,
    "HasKmLimit": 0,
    "BonusMalus": 56,
    "OutUseNb": 0,
    "RiskArea": 0
}


def send_json(data):
    """функция отправки JSON-а"""
    url = 'http://127.0.0.1:5000/predict'
    headers = {'content-type': 'application/json'}
    response = requests.post(url, json=data, headers=headers)
    return response


if __name__ == '__main__':
    RESULT = send_json(DATA)
    print(RESULT.json())
