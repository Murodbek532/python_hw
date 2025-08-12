import math

# 1. 
side = float(input("Введите сторону квадрата: "))
perimeter_square = 4 * side
area_square = side ** 2
print(f"Периметр квадрата: {perimeter_square}")
print(f"Площадь квадрата: {area_square}")

# 2. 
diameter = float(input("\nВведите диаметр круга: "))
circumference = math.pi * diameter
print(f"Длина окружности: {circumference}")

# 3. 
a = float(input("\nВведите число a: "))
b = float(input("Введите число b: "))
mean = (a + b) / 2
print(f"Среднее арифметическое: {mean}")

# 4. 
sum_ab = a + b
product_ab = a * b
square_a = a ** 2
square_b = b ** 2
print(f"Сумма: {sum_ab}")
print(f"Произведение: {product_ab}")
print(f"Квадрат a: {square_a}")
print(f"Квадрат b: {square_b}")
