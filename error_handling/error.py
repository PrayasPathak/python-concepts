def divide(num):
    while True:
        try:
            divisor = int(input("Enter the divisor: "))
            result = num / divisor
        except ValueError:
            print("Please enter a number")
        except ZeroDivisionError:
            print("Divisor cannot be zero.")
        else:
            return result


def add(num1, num2):
    try:
        return num1 + num2
    except TypeError as err:
        print(f"Please enter numbers = {err}")


print(f"Sum = {add(10, 20)}")
print(f"Sum = {add(10, 'a')}")
