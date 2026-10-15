class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
        def fuel_type(self):
            return "petrol" or "Diesel"
class Electric_Car(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size
    def fuel_type(self):    #Polymorphism-same function
        return "Electric Charge"
myTesla=Electric_Car("Tesla","Model S","85KWh")
print(myTesla.fuel_type())