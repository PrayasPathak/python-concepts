class Meta(type):
    # Called before __init__(self)
    def __new__(self, class_name, bases, attrs):
        # print(attrs)
        a = {}
        # Uppercase each attribute
        for name, value in attrs.items():
            if name.startswith("__"):
                a[name] = value
            else:
                a[name.upper()] = value
        # print(a)
        return type(class_name, bases, a)


class Dog(metaclass=Meta):
    x = 5
    y = 8

    def hello(self):
        print("hi")


d = Dog()
# print(d.x) # Does not work as the attribute is uppercased
print(d.X)
# d.hello()
d.HELLO()
