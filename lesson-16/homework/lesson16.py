import numpy as np

# 1. Convert List to 1D Array
lst = [12.23, 13.32, 100, 36.32]
arr = np.array(lst)
print("Original List:", lst)
print("One-dimensional NumPy array:", arr)


# 2. Create 3x3 Matrix (2–10)
matrix = np.arange(2, 11).reshape(3, 3)
print("\n3x3 Matrix from 2 to 10:\n", matrix)


# 3. Null Vector (10) & Update Sixth Value
null_vec = np.zeros(10)
print("\nNull Vector:", null_vec)
null_vec[5] = 11   # индекс 5 → шестое значение
print("After update:", null_vec)


# 4. Array from 12 to 38
arr_range = np.arange(12, 38)
print("\nArray from 12 to 38:", arr_range)


# 5. Convert Array to Float Type
arr_int = np.array([1, 2, 3, 4])
arr_float = arr_int.astype(float)
print("\nOriginal array:", arr_int)
print("Converted to float:", arr_float)


# 6. Celsius to Fahrenheit Conversion
celsius = np.array([0, 12, 45.21, 34, 99.91])
fahrenheit = celsius * 9/5 + 32
print("\nValues in Celsius:", celsius)
print("Values in Fahrenheit:", fahrenheit)


# 7. Append Values to Array
arr_append = np.array([10, 20, 30])
arr_new = np.append(arr_append, [40, 50, 60, 70, 80, 90])
print("\nOriginal array:", arr_append)
print("After append:", arr_new)


# 8. Array Statistical Functions
rand_arr = np.random.rand(10)
print("\nRandom Array:", rand_arr)
print("Mean:", np.mean(rand_arr))
print("Median:", np.median(rand_arr))
print("Standard Deviation:", np.std(rand_arr))


# 9. Find min and max in 10x10 random array
rand_matrix = np.random.rand(10, 10)
print("\n10x10 Random Matrix:\n", rand_matrix)
print("Min value:", rand_matrix.min())
print("Max value:", rand_matrix.max())


# 10. Create a 3x3x3 random array
rand_3d = np.random.rand(3, 3, 3)
print("\n3x3x3 Random Array:\n", rand_3d)
