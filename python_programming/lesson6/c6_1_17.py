"""superを使った継承元クラスのメソッドの実行"""
class Car(object):
    def __init__(self, model=None):
        self.model = model

class MyCar(Car):
    pass

class AdvancedCar(Car):
    def __init__(self, model='SUV', enable_auto_run=False):
        super().__init__(model)
        self.enable_auto_run = enable_auto_run

my_car = MyCar('sedan')
print(my_car.model)
advanced_car = AdvancedCar('SUV')
print(advanced_car.model)