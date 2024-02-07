"""初期化処理にデフォルト引数を設定する"""
class Person(object):
    def __init__(self, name='Default'):
        self.name = name
        print(self.name)
    
person = Person()