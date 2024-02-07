"""継承したメソッドの実行"""
class Car(object):
    def run(self):
        print('run')

class MyCar(Car):
    pass

car = Car()
car.run()
my_car = MyCar()
my_car.run()