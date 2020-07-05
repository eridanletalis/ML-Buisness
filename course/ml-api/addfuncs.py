"""модуль, необходимый для преобразования категориальных признаков и формирования h2o-фрейма
"""
import h2o


def mapfordictgender(gender):
    """преобразуемый признак - пол"""
    dict_gender = {'Male': 0, 'Female': 1}
    res = dict_gender.get(gender)
    return res


def mapfordictmaristat(maristat):
    """преобразуемый признак - семейное положение"""
    dictmaristat = {'Other': 0, 'Alone': 1}
    res = dictmaristat.get(maristat)
    return res


def fvehusageprofessional(vehusage):
    """преобразуемый признак - профессиональное использование"""
    if vehusage == 'Professional':
        vehusageprofessional = 1
    else:
        vehusageprofessional = 0
    return vehusageprofessional


def fvehusageprivatetriptooffice(vehusage):
    """преобразуемый признак - использование транспорта (личное+дорога до офиса)"""
    if vehusage == 'Private+trip to office':
        vehusageprivatetriptooffice = 1
    else:
        vehusageprivatetriptooffice = 0
    return vehusageprivatetriptooffice


def fvehusageprivate(vehusage):
    """преобразуемый признак - использование транспорта (личное)"""
    if vehusage == 'Private':
        vehusageprivate = 1
    else:
        vehusageprivate = 0
    return vehusageprivate


def fvehusageprofessionalrun(vehusage):
    """преобразуемый признак - профессиональное использование"""
    if vehusage == 'Professional run':
        vehusageprofessionalrun = 1
    else:
        vehusageprofessionalrun = 0
    return vehusageprofessionalrun


def returnnewh2oframe():
    """создаем h2o-фрейм"""
    columns = [
        'LicAge',
        'Gender',
        'MariStat',
        'DrivAge',
        'HasKmLimit',
        'BonusMalus',
        'OutUseNb',
        'RiskArea',
        'VehUsg_Private',
        'VehUsg_Private+trip to office',
        'VehUsg_Professional',
        'VehUsg_Professional run',
        'CSP1',
        'CSP2',
        'CSP3',
        'CSP6',
        'CSP7',
        'CSP20',
        'CSP21',
        'CSP22',
        'CSP26',
        'CSP37',
        'CSP40',
        'CSP42',
        'CSP46',
        'CSP47',
        'CSP48',
        'CSP49',
        'CSP50',
        'CSP55',
        'CSP56',
        'CSP57',
        'CSP60',
        'CSP65',
        'CSP66'
    ]
    return h2o.H2OFrame([[0,
                          0,
                          0,
                          0,
                          0,
                          0,
                          0,
                          0,
                          0,
                          0,
                          0,
                          0,
                          0,
                          0,
                          0,
                          0,
                          0,
                          0,
                          0,
                          0,
                          0,
                          0,
                          0,
                          0,
                          0,
                          0,
                          0,
                          0,
                          0,
                          0,
                          0,
                          0,
                          0,
                          0,
                          0]],
                        column_names=columns)


def processinput(json_input):
    """читаем json"""
    licage = json_input["LicAge"]
    gender = mapfordictgender(json_input["Gender"])
    maristat = mapfordictmaristat(json_input["MariStat"])
    drivage = json_input["DrivAge"]
    haskmlimit = json_input["HasKmLimit"]
    bonusmalus = json_input["BonusMalus"]
    outusenb = json_input["OutUseNb"]
    riskarea = json_input["RiskArea"]
    vehusgprivate = fvehusageprivate(json_input["VehUsage"])
    vehusgprivatetriptooffice = fvehusageprivatetriptooffice(
        json_input["VehUsage"])
    vehusgprofessional = fvehusageprofessional(json_input["VehUsage"])
    vehusgprofessionalrun = fvehusageprofessionalrun(
        json_input["VehUsage"])

    csp1 = 0
    csp2 = 0
    csp3 = 0
    csp6 = 0
    csp7 = 0
    csp20 = 0
    csp21 = 0
    csp22 = 0
    csp26 = 0
    csp37 = 0
    csp40 = 0
    csp42 = 0
    csp46 = 0
    csp47 = 0
    csp48 = 0
    csp49 = 0
    csp50 = 0
    csp55 = 0
    csp56 = 0
    csp57 = 0
    csp60 = 0
    csp65 = 0
    csp66 = 0

    frame = returnnewh2oframe()

    frame[0, 'LicAge'] = licage
    frame[0, 'Gender'] = gender
    frame[0, 'MariStat'] = maristat
    frame[0, 'DrivAge'] = drivage
    frame[0, 'HasKmLimit'] = haskmlimit
    frame[0, 'BonusMalus'] = bonusmalus
    frame[0, 'OutUseNb'] = outusenb
    frame[0, 'RiskArea'] = riskarea
    frame[0, 'VehUsg_Private'] = vehusgprivate
    frame[0, 'VehUsg_Private+trip to office'] = vehusgprivatetriptooffice
    frame[0, 'VehUsg_Professional'] = vehusgprofessional
    frame[0, 'VehUsg_Professional run'] = vehusgprofessionalrun
    frame[0, 'CSP1'] = csp1
    frame[0, 'CSP2'] = csp2
    frame[0, 'CSP3'] = csp3
    frame[0, 'CSP6'] = csp6
    frame[0, 'CSP7'] = csp7
    frame[0, 'CSP20'] = csp20
    frame[0, 'CSP21'] = csp21
    frame[0, 'CSP22'] = csp22
    frame[0, 'CSP26'] = csp26
    frame[0, 'CSP37'] = csp37
    frame[0, 'CSP40'] = csp40
    frame[0, 'CSP42'] = csp42
    frame[0, 'CSP46'] = csp46
    frame[0, 'CSP47'] = csp47
    frame[0, 'CSP48'] = csp48
    frame[0, 'CSP49'] = csp49
    frame[0, 'CSP50'] = csp50
    frame[0, 'CSP55'] = csp55
    frame[0, 'CSP56'] = csp56
    frame[0, 'CSP57'] = csp57
    frame[0, 'CSP60'] = csp60
    frame[0, 'CSP65'] = csp65
    frame[0, 'CSP66'] = csp66
    return frame
