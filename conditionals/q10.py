species=str(input('Enter species: '))
age=int(input('Enter age: '))
if(species=="dog"):
    if(age<2):
        food="puppy food"
    else:
        food="adult dog food"
    
elif(species=="cat"):
    if(age>5):
        food="Senior Cat Food"
    else:
        food="Baby Cat Food"
print("Food recommended for your pet is: ",food)