password=str(input('Enter password: '))
x=len(password)
if(x<6):
    strength="weak"
elif(x>=6 and x<=10):
    strength="medium"
else:
    strength="strong"
print("Your password strength is: ",strength)
