import random
import string
from datetime import datetime

# 1. 
name = input("Введите ваше имя: ")
birth_year = int(input("Введите год рождения: "))
current_year = datetime.now().year
age = current_year - birth_year
print(f"{name}, вам {age} лет.")

# 2. 
txt1 = 'LMaasleitbtui'
# Пример: спрятаны слова "Lamb" и "Astuti", но точный способ не указан.
# Можно извлечь только буквы на четных позициях (пример)
car1 = txt1[0::2]  
print(f"Извлечённое название авто (1): {car1}")

# 3. 
txt2 = 'MsaatmiazD'
car2 = txt2[0::2]  
print(f"Извлечённое название авто (2): {car2}")

# 4. 
txt3 = "I'am John. I am from London"
area = txt3.split("from ")[1]
print(f"Место жительства: {area}")

# 5. 
user_str = input("Введите строку: ")
print(f"Строка в обратном порядке: {user_str[::-1]}")

# 6. 
vowels = "aeiouAEIOU"
text_vowels = input("Введите текст для подсчёта гласных: ")
count = sum(1 for ch in text_vowels if ch in vowels)
print(f"Количество гласных: {count}")

# 7. 
numbers = list(map(int, input("Введите числа через пробел: ").split()))
print(f"Максимальное значение: {max(numbers)}")

# 8. 
word = input("Введите слово для проверки палиндрома: ")
if word.lower() == word.lower()[::-1]:
    print("Это палиндром.")
else:
    print("Это не палиндром.")

# 9.
email = input("Введите email: ")
domain = email.split('@')[-1]
print(f"Домен: {domain}")

# 10.
length = int(input("Введите длину пароля: "))
characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for _ in range(length))
print(f"Случайный пароль: {password}")
