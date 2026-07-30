from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def drive(self):
        pass

    @abstractmethod
    def stop(self):
        pass
class Car(Vehicle):
    def drive(self):
        print("The car is driving.")

    def stop(self):
        print("The car has stopped.")

class Motorcycle(Vehicle):
    def drive(self):
        print("The motorcycle is driving.")
    def stop(self):
        print("The motorcycle has stopped.")

car = Car()
car.drive()
car.stop()

motorcycle = Motorcycle()
motorcycle.drive()