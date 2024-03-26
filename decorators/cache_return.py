import time


def cache_return(func):
    cache_value = {}
    print(cache_value)

    def wrapper(*args, **kwargs):
        if args in cache_value:
            return cache_value[args]
        result = func(*args, **kwargs)
        cache_value[args] = result
        return result

    return wrapper


@cache_return
def long_running_function(a, b):
    time.sleep(5)
    return a + b


print(long_running_function(2, 3))
print(long_running_function(2, 3))
print(long_running_function(2, 5))
