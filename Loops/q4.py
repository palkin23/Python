string=str(input('Enter a string you want to reverse: '))
reversed_str=""
for ch in string:
    reversed_str=ch+reversed_str
print(reversed_str)
