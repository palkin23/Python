string=str(input('Enter a string : '))
for ch in string:
    if(string.count(ch)==1):
        print(ch)
        break
   