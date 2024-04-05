# class File:
#     def __init__(self, filename, method):
#         self.file = open(filename, method)

#     def __enter__(self):
#         print("Enter")
#         return self.file

#     def __exit__(self, type, value, traceback):
#         print(f"{type}, {value}, {traceback}")
#         print("Exit")
#         self.file.close()
#         if type == FileNotFoundError:
#             return True  # Signifies the exception is handled properly


# with File("context.txt", "w") as f:
#     print("Middle")
#     f.write("Context!")
#     raise FileNotFoundError()


from contextlib import contextmanager


@contextmanager
def file(filename, method):
    print("Enter")
    file = open(filename, method)
    yield file
    file.close()
    print("Exit")


with file("context.txt", "w") as f:
    print("Middle")
    f.write("Welcome")
