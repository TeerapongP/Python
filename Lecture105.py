class Vehicel:
    lisen_code = ""
    serial_code = ""
    def trun_on_air(self):
        print("Turn on Air")
class Car(Vehicel):
    pass
class Van:
    lisen_code = ""
    serial_code = ""
    def trun_on_air(self):
        print("Turn on Air")
Car1 = Car()
Car1.trun_on_air()