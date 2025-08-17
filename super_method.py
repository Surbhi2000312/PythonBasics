'''super () method is user to access methods of the parent class'''

class Car:

    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("Starting")

    @staticmethod
    def stop():
        print("Stopping")


class ToyotaCar(Car):
    def __init__(self, name,type):
        self.name = name
        super().__init__(type) #parents class ka type
        # self.type = type # Toyota Car ka type
        super().start()


car1 = ToyotaCar('Toyota',"Petrol")
print(car1.type)
