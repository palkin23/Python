#enumerate() is a built-in Python function that returns an iterable of 
# index-value pairs, making it easy to access both the index and element during iteration.

x=("mango","banana","apple")  #Tuple
y=enumerate(x)
print(y)
print(list(y))  #list with key
##other way-manually index
for i in range(len(x)):
    print(i,x[i])