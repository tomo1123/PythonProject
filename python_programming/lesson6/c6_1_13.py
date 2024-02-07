"""クラスの継承"""
class Car(object):
    def run(self):
        print('run')

class AdvancedCar(Car):
    def auto_run(self):
        print('auto run')

advanced_car = AdvancedCar()
advanced_car.run()
advanced_car.auto_run()