# task 1
def is_leap(year):
    if not isinstance(year, int):
        raise ValueError("Year must be an integer.")

    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# task 2
def weird_or_not(n):
    if n % 2 == 1:
        print("Weird")
    elif 2 <= n <= 5:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    else:  
        print("Not Weird")

# Example:
weird_or_not(3)   
weird_or_not(24) 

# task 3
def even_numbers_if_else(a, b):
    if a % 2 != 0: 
        a += 1
    return list(range(a, b+1, 2))


print(even_numbers_if_else(3, 10)) 
