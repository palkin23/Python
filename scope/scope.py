username="chaiaurcode"
def func():
    username="chai"
    print(username)
print(username)
func() 

def f1():
    x=88
    def f2():
        print(x)
    f2()
f1()

def f3(num):
    def actual(x):
        return x**num
    return actual
f=f3(2)
g=f3(3)
print(f(3))
print(g(3))