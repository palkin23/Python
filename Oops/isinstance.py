class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Electric_Car(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

car1 = Electric_Car("Tata", "Safari", "60 kWh")
print(isinstance(car1,Electric_Car))
print(isinstance(car1,Car))
#isinstance() function is used to check whteher an object is instance of that class or not