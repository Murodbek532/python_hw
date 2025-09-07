
python -m venv venv


venv\Scripts\activate

source venv/bin/activate

pip install requests numpy

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for ch in s if ch in vowels)
geometry/
    __init__.py
    circle.py

from .circle import calculate_area, calculate_circumference
import math

def calculate_area(radius):
    return math.pi * radius * radius

def calculate_circumference(radius):
    return 2 * math.pi * radius
file_operations/
    __init__.py
    file_reader.py
    file_writer.py
from .file_reader import read_file
from .file_writer import write_file
def read_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()
def write_file(file_path, content):
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

import math_operations as mo
import string_utils as su
from geometry import calculate_area, calculate_circumference
from file_operations import read_file, write_file

print(mo.add(5, 3))                 
print(su.reverse_string("hello"))   
print(su.count_vowels("assalom"))     
print(calculate_area(5))              
print(calculate_circumference(5))     


write_file("test.txt", "Hello world!")
print(read_file("test.txt"))         
