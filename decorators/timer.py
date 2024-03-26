# Simple decorator to compute the time taken by a function to execute
from functools import reduce
from time import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time()
        func(*args, **kwargs)
        end = time()
        result = end - start
        print(f"The {func.__name__} took {result}s to complete execution")

    return wrapper


@timer
def long_run(n):
    sum = reduce(lambda acc, x: acc + x, range(1, n))
    print(f"Sum = {sum}")


num = int(input("Enter the number up to which sum needs to be computed: "))
long_run(num)
