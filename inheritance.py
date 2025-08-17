
"""Single and  Multilevel Inheritance"""
class Car:
    @staticmethod
    def start():
        print("Starting")

    @staticmethod
    def stop():
        print("Stopping")


class ToyotaCar(Car):
    def __init__(self, brand):
        self.brand = brand

# car1 = ToyotaCar("Fortuner")
# car2 = ToyotaCar("Prius")

# car1.start()

class Fortuner(ToyotaCar):
    def __init__(self, type):
        self.type = type

car = Fortuner("diesel")
car.start()

