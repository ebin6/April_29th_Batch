'''from abc import ABC,abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    def display(self):
        print("Hello")
class Bike(Vehicle):
    def start(self):
        print("Bike starts")
v=Bike()'''
from abc import ABC,abstractmethod
class Payments(ABC):
    @abstractmethod
    def process(self):
        pass


class GPay(Payments):
    def process(self):
        print("Gpay mode")
class PhonePay(Payments):
    def process(self):
        print("PhonePay mode")

g_obj=GPay()  # Object creation
g_obj.process()

p_obj=PhonePay()
p_obj.process()