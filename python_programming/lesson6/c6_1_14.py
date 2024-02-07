"""メソッドのオーバーライド"""
class Car(object):
    def run(self):
        print('run')

class MyCar(Car):
    def run(self):
        print('fast')

class AdvancedCar(Car):
    def run(self):
        print('super fast')

car = Car()
car.run()
print('##########')
my_car = MyCar()
my_car.run()
print('##########')
advanced_car = AdvancedCar()
advanced_car.run()