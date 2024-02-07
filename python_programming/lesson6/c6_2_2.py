"""オブジェクトの変数に_をつける"""
class Car(object):
    def __init__(self, model=None):
        self.model = model

class AdvancedCar(Car):
    def __init__(self, model='SUV', enable_auto_run=False):
        super().__init__(model)
        self._enable_auto_run = enable_auto_run

advanced_car = AdvancedCar('SUV')
advanced_car._enable_auto_run = True
print(advanced_car._enable_auto_run)