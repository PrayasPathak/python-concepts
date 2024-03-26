from functools import reduce

# map, filter, reduce, zip


# map(action, data)
def multiply_by_2(item):
    return item * 2


# Map
nums = [10, 2, 123]
print(f"Nums = {nums}")
print(map(multiply_by_2, [10, 20, 30]))
print(list(map(multiply_by_2, nums)))
print(f"Nums = {nums}")


# filter
def check_odd(item):
    return item % 2 != 0


print(filter(check_odd, nums))
print(list(filter(check_odd, nums)))

users = [
    {"name": "Tom", "is_employed": False},
    {"name": "Matt", "is_employed": True},
    {"name": "Alice", "is_employed": False},
    {"name": "Jane", "is_employed": True},
    {"name": "Henry", "is_employed": False},
]


def check_employement_status(item):
    return item["is_employed"] == True


print(list(filter(check_employement_status, users)))


# Zip
my_list = [10, 20, 30]
your_list = [34, 62, 66]

print(list(zip(my_list, your_list)))
print(list(zip(my_list, users)))


# Reduce
def accumulator(acc, item):
    print(acc, item)
    return acc + item


print(reduce(accumulator, nums, 0))
