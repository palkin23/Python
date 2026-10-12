class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def full_name(self):
        print(self.brand," ",self.model)
class Electric_Car(Car):
    def __init__(self,brand,model,batterysize):
        super().__init__(brand,model)
        self.batterysize=batterysize
mytesla=Electric_Car("Tesla","Model S","85KWh")
print(mytesla.model)
mytesla.full_name()
              