class Vehicle():
    def __init__(self, bodystyle):
        self.bodystyle = bodystyle


# a subclass that inherits Vehicle
class Car(Vehicle):
    def __init__(self, enginetype):
        #Call the super class to init a car class
        super().__init__("Car")
        self.wheels = 4
        self.doors = 4
        self.enginetype = enginetype

# a subclass that inherits Vehicle
class Motorcycle(Vehicle):
    def __init__(self, enginetype, hassidecar):
        super().__init__("Motorcyle")
        if (hassidecar):
            self.wheels = 3
        else:
            self.wheels = 2
        self.doors = 0
        self.enginetype = enginetype

car1 = Car("gas")
car2 = Car("electric")
mc1 = Motorcycle('gas', True)

print(mc1.wheels)
print(car1.enginetype)
print(car2.doors)