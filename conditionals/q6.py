distance=int(input('Enter distance: '))
if(distance<3):
    activity="walk"
elif(distance<15):
    activity="bike"
else:
    activity="car"
print("Recommended mode of travel is : ",activity)