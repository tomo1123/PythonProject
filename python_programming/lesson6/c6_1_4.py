"""初期化処理"""
class Person(object):
    def __init__(self, name):
        self.name = name
        print(self.name)
    
person = Person('Mike')