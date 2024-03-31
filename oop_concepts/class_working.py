# Understanding how classes works under the hood

# class Test:
#     pass


# Checking type
# print(type(Test()))
# print(type(Test))

# print(type(int))

# Equivalent of Creating class


class Demo:
    def demo(self):
        print("This is a dummy method")


def add_attribute(self):
    self.z = 19


Test = type("Test", (Demo,), {"x": 5, "add_attribute": add_attribute})
"""
# Is equivalent to
class Test: 
    pass
"""
print(type(Test))
print(Test())
t = Test()
print(t.x)
t.x = 100
t.y = 20
print(f"x = {t.x}, y = {t.y}")
t.demo()
t.add_attribute()
print(f"z = {t.z}")
