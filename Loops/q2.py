n=int(input('Enter n: '))
sum=0
#n+1 as last is not included
for num in range(1,n+1):
  if(num%2==0):
    sum=sum+num
print("Sum of even numbers till n is : ",sum)
     

