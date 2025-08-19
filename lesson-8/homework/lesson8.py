# 1. ZeroDivisionError
try:
    num = 10 / 0
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

# 2. ValueError for integer input
try:
    n = int(input("Enter an integer: "))
except ValueError:
    print("Error: That is not a valid integer.")

# 3. FileNotFoundError
try:
    with open("nonexistent.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("Error: File not found.")

# 4. TypeError for non-numerical input
try:
    a = input("Enter first number: ")
    b = input("Enter second number: ")
    result = float(a) + float(b)
except ValueError:
    raise TypeError("Inputs must be numerical.")

# 5. PermissionError
try:
    with open("/root/protected.txt", "w") as f:
        f.write("test")
except PermissionError:
    print("Error: Permission denied.")

# 6. IndexError
numbers = [1, 2, 3]
try:
    print(numbers[5])
except IndexError:
    print("Error: Index out of range.")

# 7. KeyboardInterrupt
try:
    num = input("Enter a number (press Ctrl+C to cancel): ")
except KeyboardInterrupt:
    print("\nInput cancelled by user.")

# 8. ArithmeticError
try:
    x = 10 / 0
except ArithmeticError:
    print("Arithmetic error occurred.")

# 9. UnicodeDecodeError
try:
    with open("file.txt", encoding="ascii") as f:
        print(f.read())
except UnicodeDecodeError:
    print("Error: Encoding issue with file.")

# 10. AttributeError
my_list = [1, 2, 3]
try:
    my_list.push(4)  # push does not exist in Python lists
except AttributeError:
    print("Error: Attribute does not exist.")
# 1. Read entire file
with open("sample.txt", "r") as f:
    print(f.read())

# 2. Read first n lines
n = 3
with open("sample.txt", "r") as f:
    for i in range(n):
        print(f.readline().strip())

# 3. Append text and display
with open("sample.txt", "a") as f:
    f.write("\nAppended line.")
with open("sample.txt", "r") as f:
    print(f.read())

# 4. Read last n lines
n = 2
with open("sample.txt", "r") as f:
    lines = f.readlines()
    print("".join(lines[-n:]))

# 5. Read file line by line into list
with open("sample.txt", "r") as f:
    lines_list = f.readlines()
print(lines_list)
# 6. Read file line by line into a variable (single string)
with open("sample.txt", "r") as f:
    data = f.read()
print(data)

# 7. Read file line by line into an array
with open("sample.txt", "r") as f:
    arr = [line.strip() for line in f]
print(arr)

# 8. Find the longest words
with open("sample.txt", "r") as f:
    words = f.read().split()
    longest = max(words, key=len)
print("Longest word:", longest)

# 9. Count number of lines
with open("sample.txt", "r") as f:
    line_count = sum(1 for _ in f)
print("Number of lines:", line_count)

# 10. Count word frequency
from collections import Counter
with open("sample.txt", "r") as f:
    words = f.read().replace(",", " ").split()
    freq = Counter(words)
print(freq)

# 11. Get file size
import os
size = os.path.getsize("sample.txt")
print("File size:", size, "bytes")

# 12. Write a list to file
mylist = ["apple", "banana", "cherry"]
with open("list.txt", "w") as f:
    for item in mylist:
        f.write(item + "\n")

# 13. Copy file contents
with open("sample.txt", "r") as src, open("copy.txt", "w") as dst:
    dst.write(src.read())

# 14. Combine lines from two files
with open("file1.txt") as f1, open("file2.txt") as f2:
    for line1, line2 in zip(f1, f2):
        print(line1.strip() + " " + line2.strip())

# 15. Read a random line
import random
with open("sample.txt") as f:
    lines = f.readlines()
    print(random.choice(lines))

# 16. Check if file is closed
f = open("sample.txt", "r")
print(f.closed)  # False
f.close()
print(f.closed)  # True

# 17. Remove newline characters
with open("sample.txt") as f:
    content = f.read().replace("\n", " ")
print(content)

# 18. Count words in a file
with open("sample.txt") as f:
    text = f.read().replace(",", " ")
    words = text.split()
print("Word count:", len(words))

# 19. Extract characters into list
chars = []
for filename in ["file1.txt", "file2.txt"]:
    with open(filename) as f:
        chars.extend(list(f.read()))
print(chars)

# 20. Generate 26 text files (A.txt, B.txt, …, Z.txt)
import string
for letter in string.ascii_uppercase:
    with open(f"{letter}.txt", "w") as f:
        f.write(f"This is file {letter}\n")

# 21. Create alphabet file with N letters per line
import string
n = 5
letters = string.ascii_uppercase
with open("alphabet.txt", "w") as f:
    for i in range(0, len(letters), n):
        f.write(" ".join(letters[i:i+n]) + "\n")
