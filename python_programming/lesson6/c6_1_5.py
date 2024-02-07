"""初期化時に引数を渡す"""
class Person(object):
    def __init__(self, name):
        self.name = name
        print(self.name)
    
person = Person()