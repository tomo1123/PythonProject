"""親クラスで__init__を定義する"""
class Car(object):
    def __init__(self, model=None):
        self.model = model

class MyCar(Car):
    pass

class AdvancedCar(Car):
    pass

my_car = MyCar('sedan')
print(my_car.model)
advanced_car = AdvancedCar('SUV')
print(advanced_car.model)