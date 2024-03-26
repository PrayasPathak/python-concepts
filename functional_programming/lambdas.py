from functools import reduce

# Lambdas: Anonymous functions used only once

# lambda param: action(param)

nums = [10, 23, 65, 12, 78, 17]
doubled_numbers = map(lambda item: item * 2, nums)
print(f"Nums = {nums}")
print(f"Doubled Numbers = {list(doubled_numbers)}")

# Odd Numbers
odd_numbers = filter(lambda item: item % 2 != 0, nums)
print(f"Odd numbers = {list(odd_numbers)}")

# Reduced
print(reduce(lambda acc, x: x + acc, nums, 10))

# Exercise
squared_numbers = list(map(lambda x: x**2, nums))
print(f"Squared Numbers = {squared_numbers}")

# List Sorting
# Sort the list on the basis of the second value
a = [(0, 2), (4, 3), (9, 9), (10, -1)]
print(f"Before sorting: {a}")
a.sort(key=lambda x: x[1])
print(f"After sorting: {a}")
