n=int(input('Enter a number: '))
while(n<1 or n>10):
    print("Enter the input number again: ")
    n = int(input("Enter a number between 1 and 10: "))
print("Valid Input: ",n)