"""модуль, необходимый для теста категориальных признаков"""

from addfuncs import mapfordictgender


def test_map_for_dict_Gender():
    """функция теста категориального признака"""
    assert mapfordictgender('Male') == 0
    assert mapfordictgender('Female') == 1
