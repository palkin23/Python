class Car:
    def __init__(self,brand,model):
        self.__brand=brand    #private
        self.model=model
    def get__brand(self):
        return self.__brand+"!"
mycar=Car("Tesla","Model S")
print(mycar.get__brand())

