import time
def cache(func):
    cache_value={} #dictionary-easy in memory
    print(cache_value)
    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]
        result=func(*args)
        cache_value[args]=result
        return result
    return wrapper
@cache
def long_running_func(a,b):
    time.sleep(4)
    return a+b
print(long_running_func(2,3))
print(long_running_func(2,3))
print(long_running_func(4,3))
#o/p first {} because 4 sec buffer nothing excecuted
#so empty {}-long running func
#then after 4sec -2 times 5
#then after 4 sec-7