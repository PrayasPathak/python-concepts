# List comprehension
# param for param in iterable if condition

nums = [i for i in range(1, 10)]
print(f"Nums = {nums}")

characters = [char for char in "welcome home"]
print(f"Characters = {characters}")

doubled_numbers = [i * 2 for i in range(1, 101)]
print(f"Doubled Numbers = {doubled_numbers}")

odd_numbers = [i for i in range(1, 100) if 1 % 2 != 0]
print(f"Odd Numbers = {odd_numbers}")


# Set comprehension
# Similar to list comprehension. Just replace [] with {}


# Dictionary Comprehension
dict = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
my_dict = {key: value**2 for key, value in dict.items() if value % 2 == 0}
print(my_dict)


dict = {num: num * 2 for num in [1, 2, 3]}
print(f"Dict = {dict}")


# Find duplicates from the list
some_list = ["a", "b", "c", "d", "e", "f", "d", "b", "e", "a", "c"]
duplicate_items = set([item for item in some_list if some_list.count(item) > 1])
duplicate_items = list(duplicate_items)
print(f"Duplicate Items = {duplicate_items}")
