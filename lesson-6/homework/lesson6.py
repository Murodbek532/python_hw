
def modify_string(txt):
    vowels = "aeiou"
    result = []
    count = 0

    i = 0
    while i < len(txt):
        result.append(txt[i])
        count += 1

        if count == 3:
            if txt[i] not in vowels and (i + 1 >= len(txt) or txt[i+1] != "_"):
                result.append("_")
            count = 0
        i += 1

    if result and result[-1] == "_":
        result.pop()

    return "".join(result)


# Examples
print(modify_string("hello"))          
print(modify_string("assalom"))         
print(modify_string("abcabcabcdeabcdefabcdefg"))  

def integer_squares(n):
    for i in range(n):
        print(i**2)

# Example:
integer_squares(5)


# Exercise 1
i = 1
while i <= 10:
    print(i)
    i += 1

# Exercise 2
for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

# Exercise 3
n = 10
print("Sum is:", sum(range(1, n+1)))

# Exercise 4
num = 2
for i in range(1, 11):
    print(num * i)

# Exercise 5
numbers = [12, 75, 150, 180, 145, 525, 50]
for num in numbers:
    if num % 5 == 0 and num < 500:
        print(num)

# Exercise 6
num = 75869
print("Digits:", len(str(num)))

# Exercise 7
for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()

# Exercise 8
list1 = [10, 20, 30, 40, 50]
for item in reversed(list1):
    print(item)

# Exercise 9
for i in range(-10, 0):
    print(i)

# Exercise 10
for i in range(5):
    print(i)
print("Done!")

# Exercise 11 (prime numbers in range)
start, end = 25, 50
print("Prime numbers between", start, "and", end, ":")
for num in range(start, end+1):
    if num > 1:
        for j in range(2, int(num**0.5)+1):
            if num % j == 0:
                break
        else:
            print(num)

# Exercise 12 Fibonacci (10 terms)
a, b = 0, 1
print("Fibonacci sequence:")
for _ in range(10):
    print(a, end=" ")
    a, b = b, a + b
print()

# Exercise 13 Factorial
n = 5
fact = 1
for i in range(1, n+1):
    fact *= i
print(f"{n}! =", fact)


def uncommon_elements(list1, list2):
    from collections import Counter
    c1, c2 = Counter(list1), Counter(list2)
    result = []

    for elem in (c1 - c2).elements():
        result.append(elem)
    for elem in (c2 - c1).elements():
        result.append(elem)

    return result


print(uncommon_elements([1, 1, 2], [2, 3, 4]))            
print(uncommon_elements([1, 2, 3], [4, 5, 6]))            
print(uncommon_elements([1, 1, 2, 3, 4, 2], [1, 3, 4, 5]))
