# 1. Sort a Dictionary by Value
d = {1: 2, 3: 1, 4: 5, 2: 4}
asc = dict(sorted(d.items(), key=lambda x: x[1]))
desc = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
print("Ascending:", asc)
print("Descending:", desc)

# 2. Add a Key to a Dictionary
d = {0: 10, 1: 20}
d[2] = 30
print("Dictionary after adding key:", d)

# 3. Concatenate Multiple Dictionaries
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
merged = {}
for dic in (dic1, dic2, dic3):
    merged.update(dic)
print("Merged dictionary:", merged)

# 4. Generate a Dictionary with Squares
n = 5
squares = {x: x**2 for x in range(1, n+1)}
print("Squares dictionary (1..5):", squares)

# 5. Dictionary of Squares (1 to 15)
squares_15 = {x: x**2 for x in range(1, 16)}
print("Squares dictionary (1..15):", squares_15)


# 1. Create a Set
myset = {1, 2, 3, 4}
print("Created set:", myset)

# 2. Iterate Over a Set
for item in myset:
    print("Iterating:", item)

# 3. Add Member(s) to a Set
myset.add(5)
myset.update([6, 7])
print("After adding:", myset)

# 4. Remove Item(s) from a Set
myset.remove(3)   # если 3 нет -> ошибка
print("After removing 3:", myset)

# 5. Remove an Item if Present in the Set
myset.discard(10)  # если 10 нет -> не ошибка
print("After discarding 10:", myset)
