class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def func(self):
        print(self.brand)

c1=Car("Ferrari", "296 GTB")
print(c1.brand," ",c1.model)
c1.func()