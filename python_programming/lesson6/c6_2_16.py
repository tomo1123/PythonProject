"""メソッドがないとエラーになる"""
class Person(object):
    def __init__(self, age=1):
        self.age = age

class Adult(Person):
    def __init__(self, age=18):
        if age >= 18:
            super().__init__(age)
        else:
            raise ValueError

adult = Adult()
adult.drive()