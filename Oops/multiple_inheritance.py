class Engine:
    def print(self):
        return "engine class"
class Battery:
    def print1(self):
        return "battery class"
class Car(Engine,Battery):
    pass
mycar=Car()
print(mycar.print())
print(mycar.print1())