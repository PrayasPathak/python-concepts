"""
Properties of Pure function

1. A pure function always returns the same output given the same output. 
2. A pure function should not have any side effect (i.e should not affect outside world.)

"""


# Is a pure function as it does not interact with anything outside of its scope.
def multiply_by_2(li):
    new_list = []
    for item in li:
        new_list.append(item * 2)
    return new_list


if __name__ == "__main__":
    li = [10, 30, 50]
    result = multiply_by_2(li)
    print(f"New List = {result}")
