"""引数を取るスタティックメソッド"""
class Person(object):

    @staticmethod
    def about(year):
        print('about human {}'.format(year))

Person.about(1999)