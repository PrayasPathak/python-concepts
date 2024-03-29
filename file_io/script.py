# Reading a file

# file = open("demo.txt")
# print(type(file))
# data = file.read()
# print(f"Data = {data}, Type = {type(data)}")

# Placing the cursor to the start of the file
# file.seek(0)
# Iterating the file line by line
# lines = file.readlines()
# for line in lines:
#     print(line, sep="")
# file.close()


# Writing to a file
# file = open("data.txt", "a")
# message = input("Enter the message to be stored in the file: ")
# file.write(f"{message}\n")
# print(f"Data wrote successfully")
# file.close()
while True:
    try:
        file_path = input("Enter the path to the file: ")
        with open(file_path, "r") as f:
            data = f.read()
            print(data)
    except FileNotFoundError:
        print(
            f"The file you're looking for does not exist. Please provide a valid file"
        )
    else:
        break
