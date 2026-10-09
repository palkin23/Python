order_size=str(input('Enter your coffee order size: '))
extra_shot=input("Do you need an extra shot? (yes/no): ")
if(extra_shot=="yes"):
    coffee=order_size+" +Extra shot of expresso"
else:
    coffee=order_size
print("Your order is: ",coffee)