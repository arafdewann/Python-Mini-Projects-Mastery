#Basic of Python Programming
# Variables and basic data types
name = "Arafat"  # String variable
age = 25  # Integer variable
is_student = True  # Boolean variable

# Conditional statements (if-else)
if age < 18:
    print(f"{name} is a minor.")
else:
    print(f"{name} is an adult.")

# Function with parameters and return value
def greet(person_name):
    return f"Hello, {person_name}!"

# Calling the function
print(greet(name))

# Lists (arrays)
fruits = ["apple", "banana", "cherry"]

# Looping through a list
for fruit in fruits:
    print(f"I like {fruit}")

# While loop with a counter
counter = 0
while counter < 3:
    print(f"Counter is at {counter}")
    counter += 1  # Increment the counter

# File handling (writing and reading a file)
with open("example.txt", "w") as file:  # 'w' for writing
    file.write("This is a test file.")

# Reading the file
with open("example.txt", "r") as file:  # 'r' for reading
    content = file.read()
    print("File content:", content)

# List comprehension (concise way to create lists)
squares = [x**2 for x in range(5)]  # Generates squares of numbers from 0 to 4
print("Squares:", squares)
