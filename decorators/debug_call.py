# A decorator to print the name of the function along with the parameters passed to the function


def debug(func):
    def wrapper(*args, **kwargs):
        args_value = ", ".join(str(arg) for arg in args)
        kwargs_value = ", ".join(f"{k}={v}" for k, v in kwargs.items())
        print(
            f"Calling {func.__name__} with args {args_value} and kwargs {kwargs_value}"
        )
        return func(*args, **kwargs)

    return wrapper


@debug
def hello():
    print("Hello")


hello()


@debug
def greet(name, greeting="Hello", email=""):
    print(f"{greeting}, {name}. Your email is {email}")


name = input("Enter your name: ")
greeting = input("Enter your greeting: ")
email = input("Enter your email: ")
greet(name, greeting=greeting, email=email)
