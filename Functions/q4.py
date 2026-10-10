import math
def Circle(radius):
    circumfrence=2*math.pi*radius
    area = math.pi* radius**2
    return circumfrence,area
c,a=Circle(4)
print("Circumfrence: ",c,"\nArea: ",a)