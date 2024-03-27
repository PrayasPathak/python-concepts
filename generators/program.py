# Generator:
# allows to generate a sequence of values over time
# can pause and resume functions


def make_list(num):
    """
    Creates a list upto the specified number by increasing each number by 5 and returns the list.
    """
    result = []
    for i in range(num):
        result.append(i + 5)
    return result


my_list = make_list(10000)  # Lives in memory
print(f"My List = {my_list}")


def generator_func(num):
    """
    Loops through each number in the specified range and returns them one at a time.
    """
    for i in range(num):
        yield i  # Pauses the function and returns when next() is called


# for item in generator_func(10000000):
#     print(item)
# Keeps one item in memory instead of entire list


g = generator_func(10000000)
print(g)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
