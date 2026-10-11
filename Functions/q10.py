def recursive_fact(n):
    if n==0:
        return 1
    else:
        return n*recursive_fact(n-1)
print(recursive_fact(5))