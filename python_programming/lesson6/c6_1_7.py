"""オブジェクトの変数を呼び出す"""
class Person(object):
    def __init__(self, name):
        self.name = name

    def say_something(self):
        print('I am {}. hello'.format(self.name))
    
person = Person('Mike')
person.say_something()