import inspect


class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Person({ self.name })"

    def __mul__(self, x):
        if type(x) is not int:
            raise ValueError("Invalid argument, value must be int")
        self.name = self.name * x

    def __call__(self, y):
        print(y)

    def __len__(self):
        return len(self.name)


person = Person("Mike")
# print(inspect.getmembers(person))
print(person)
person * 4
print(person)

person(4)
