"""クラスメソッド"""
class Person(object):
    kind = 'human'

    def __init__(self):
        self.x = 100

    @classmethod
    def what_is_your_kind(cls):
        return cls.kind

print(Person.kind)
print(Person.what_is_your_kind())