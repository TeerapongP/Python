
class Vehicle:
    lecenseCode = ""
    serialCode = ""
    def turnOnAirConditioner(self):
        print("Turn On : Air")

class Car(Vehicle): #สืบทอดจาก Vehicle
    pass

class Pickup(Vehicle):
    pass

class Van(Vehicle):
    pass

class Estatecar(Vehicle):
    pass

def inherit():
    Pickup1 = Pickup()
    car1 = Car()
    Van1 = Van()

    Estatecar1 = Estatecar()
    car1.turnOnAirConditioner()
    Pickup1.turnOnAirConditioner()
    car1.turnOnAirConditioner()
    Van1.turnOnAirConditioner()
    Estatecar1.turnOnAirConditioner()

inherit()