class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    @staticmethod
    def general_des():
        return "We are learning abput static methods"
Safari=Car("Tata","Safari")
print(Car.general_des())
print(Safari.general_des())