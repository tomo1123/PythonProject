"""クラスの定義と利用"""
class Person(object):
    kind = 'human'

    def __init__(self):
        self.x = 100

a = Person()
print(a)
b = Person
print(b)