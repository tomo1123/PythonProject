"""インスタンス変数の呼び出し"""
class Person(object):
    kind = 'human'

    def __init__(self):
        self.x = 100

a = Person()
print(a.x)