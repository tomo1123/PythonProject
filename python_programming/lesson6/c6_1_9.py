"""デストラクタ"""
class Person(object):
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print('good bye')

person = Person('Mike')
print('##########')