def main():
    x = get_int("What's X? ")
    print(f"X = {x}")


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a number")
        finally:
            print(f"Finally done")


main()
