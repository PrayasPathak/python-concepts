from time import time


def performance(func):
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(f"{func.__name__} took {end-start}s to complete execution")
        return result

    return wrapper


@performance
def long_time():
    for i in range(100000000):
        i + 10


@performance
def greet(name):
    print(f"Hello, {name}")


@performance
def long_time2():
    for i in list(range(100000000)):
        i + 5


long_time()
greet("User")
long_time2()
