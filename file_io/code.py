# Write the data to the file. Name of the file should be practice.txt
def write_data_to_file():
    while True:
        try:
            file_path = input("Enter the file path: ")
            file = open(file_path, "w")
            file.write("Hi everyone\ni am learning File I/O\n")
            file.write("using Java.\nI like Java programming language")
        except FileNotFoundError:
            print("File does not exist. Please provide a valid file path.")
        finally:
            file.close()
            print(f"Data wrote successfully.")
            break


# Replace all occurrences of java with python in file
def replace_word_occurrences():
    with open("practice.txt", "r") as file:
        data = file.read()

    new_data = data.replace("Java", "Python")
    with open("practice.txt", "w") as file:
        file.write(new_data)


# Search whether the word 'learning' exists in the file or not
def check_for_word():
    with open("practice.txt", "r") as file:
        data = file.read()
        word = input("Enter the word to be searched in the file: ")
        index = data.find(word)
        if index != -1:
            print(f"Word found at index {index}")
        else:
            print("The word does not exist in the file.")


def check_for_line():
    word = input("Enter the word to be searched: ")
    data = True
    line_number = 1
    with open("practice.txt", "r") as file:
        while data:
            data = file.readline()
            if word in data:
                print(f"Word exists at line {line_number}")
            line_number += 1

    return -1


def find_even_numbers():
    count = 0
    with open("data.txt", "r") as file:
        data = file.read()
        print(data)
        nums = data.split(",")
        for num in nums:
            if int(num) % 2 == 0:
                count += 1

    return count


print(f"Even numbers = {find_even_numbers()}")
