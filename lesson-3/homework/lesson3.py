# 1. 
fruits = ["apple", "banana", "cherry", "mango", "grape"]
print("3-й фрукт:", fruits[2])

# 2. 
list1 = [1, 2, 3]
list2 = [4, 5, 6]
concatenated = list1 + list2
print("Объединённый список:", concatenated)

# 3.
numbers = [10, 20, 30, 40, 50]
middle_index = len(numbers) // 2
new_list = [numbers[0], numbers[middle_index], numbers[-1]]
print("Новый список:", new_list)

# 4. 
movies = ["Inception", "Titanic", "Avatar", "Matrix", "Gladiator"]
movies_tuple = tuple(movies)
print("Кортеж фильмов:", movies_tuple)

# 5. 
cities = ["London", "Paris", "Berlin", "Rome"]
print("Париж в списке?", "Paris" in cities)

# 6. 
nums = [1, 2, 3]
duplicated = nums * 2
print("Дубликат списка:", duplicated)

# 7. 
nums_swap = [5, 6, 7, 8, 9]
nums_swap[0], nums_swap[-1] = nums_swap[-1], nums_swap[0]
print("После обмена:", nums_swap)

# 8. 
tuple_numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print("Срез (3–7):", tuple_numbers[3:8])

# 9. 
colors = ["blue", "red", "blue", "green", "blue", "yellow"]
print("Слово 'blue' встречается:", colors.count("blue"), "раз(а)")

# 10. 
animals = ("cat", "dog", "lion", "tiger")
print("Индекс 'lion':", animals.index("lion"))

# 11. 
t1 = (1, 2, 3)
t2 = (4, 5, 6)
merged_tuple = t1 + t2
print("Объединённый кортеж:", merged_tuple)

# 12.
lst = [1, 2, 3, 4]
tpl = (5, 6, 7)
print("Длина списка:", len(lst))
print("Длина кортежа:", len(tpl))

# 13. 
tuple_nums = (10, 20, 30, 40, 50)
list_from_tuple = list(tuple_nums)
print("Кортеж в список:", list_from_tuple)

# 14. 
tuple_vals = (15, 3, 9, 27, 5)
print("Максимум:", max(tuple_vals))
print("Минимум:", min(tuple_vals))

# 15.
words_tuple = ("one", "two", "three", "four")
print("В обратном порядке:", words_tuple[::-1])
