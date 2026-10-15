class Car:
    total_Car = 0

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.total_Car += 1
Safari=Car("Tata","Safari")
Tesla=Car("Tesla","Model S")
print(Car.total_Car)