"""オブジェクトからメソッドを実行"""
class Person(object):
    kind = 'human'

    def __init__(self):
        self.x = 100

    def what_is_your_kind(self):
        return self.kind

a = Person()
print(a.what_is_your_kind())