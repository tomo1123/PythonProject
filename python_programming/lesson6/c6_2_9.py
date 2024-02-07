"""__をつけた変数にクラス内からアクセスする"""
class Car(object):
    def __init__(self, model=None):
        self.model = model

class AdvancedCar(Car):
    def __init__(self, model='SUV', enable_auto_run=False):
        super().__init__(model)
        self.__enable_auto_run = enable_auto_run

    @property
    def enable_auto_run(self):
        return self.__enable_auto_run

    def run(self):
        print(self.__enable_auto_run)
        print('super fast')

advanced_car = AdvancedCar('SUV')
advanced_car.run()