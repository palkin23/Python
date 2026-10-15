class Car:
    def __init__(self, brand,model):
        self.__brand=brand
        self.__model=model
    def get_attributes(self):
        return f"{self.__brand},{self.__model}"
    @property
    def model(self):
        return self.__model
Mycar=Car("Tata","Safari")

print(Mycar.get_attributes())