def add(a, b):
    """Add two numbers"""
    return a + b


def subtract(a, b):
    """Subtract two nummbers"""
    return a - b


def multiply(a, b):
    """Multiply two numbers"""
    return a * b


def divide(a, b):
    """Divide two numbers"""
    if b == 0:
        raise ValueError("Can not divide by zero!")
    return a // b
