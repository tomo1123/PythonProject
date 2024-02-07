"""モジュールの読み込みと呼び出し"""
from lesson_package.tools import utils
# from ..tools import utils

def sing():
    return 'sing'

def cry():
    return utils.say_twice('cry')
    # return 'cry'