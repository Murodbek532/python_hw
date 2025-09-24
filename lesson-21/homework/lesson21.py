import pandas as pd
import matplotlib.pyplot as plt

# DataFrame 1: Student Grades
data1 = {
    'Student_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Math': [85, 90, 78, 92, 88, 95, 89, 79, 83, 91],
    'English': [78, 85, 88, 80, 92, 87, 90, 84, 79, 88],
    'Science': [90, 92, 85, 88, 94, 79, 83, 91, 87, 89]
}
df1 = pd.DataFrame(data1)

# 1. 
df1["Average"] = df1[["Math", "English", "Science"]].mean(axis=1)

# 2. 
top_student = df1.loc[df1["Average"].idxmax()]

# 3. 
df1["Total"] = df1[["Math", "English", "Science"]].sum(axis=1)

# 4. 
df1[["Math", "English", "Science"]].mean().plot(kind="bar", title="Average Grades by Subject")
plt.ylabel("Average Grade")
plt.show()

print("Top student with highest average:\n", top_student, "\n")

# DataFrame 2: Sales Data
data2 = {
    'Date': pd.date_range(start='2023-01-01', periods=10),
    'Product_A': [120, 150, 130, 110, 140, 160, 135, 125, 145, 155],
    'Product_B': [90, 110, 100, 80, 95, 105, 98, 88, 102, 112],
    'Product_C': [75, 80, 85, 70, 88, 92, 78, 82, 87, 90]
}
df2 = pd.DataFrame(data2)

# 1. 
total_sales = df2[["Product_A", "Product_B", "Product_C"]].sum()

# 2. 
df2["TotalSales"] = df2[["Product_A", "Product_B", "Product_C"]].sum(axis=1)
date_max_sales = df2.loc[df2["TotalSales"].idxmax(), "Date"]

# 3. 
pct_change = df2[["Product_A", "Product_B", "Product_C"]].pct_change() * 100

# 4. 
df2.plot(x="Date", y=["Product_A", "Product_B", "Product_C"], marker="o", title="Sales Trends Over Time")
plt.ylabel("Sales")
plt.show()

print("Total sales:\n", total_sales, "\n")
print("Date with highest sales:", date_max_sales, "\n")

# DataFrame 3: Employee Information
data3 = {
    'Employee_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Hank', 'Ivy', 'Jack'],
    'Department': ['HR', 'IT', 'Marketing', 'IT', 'Finance', 'HR', 'Marketing', 'IT', 'Finance', 'Marketing'],
    'Salary': [60000, 75000, 65000, 80000, 70000, 72000, 68000, 78000, 69000, 76000],
    'Experience (Years)': [3, 5, 2, 8, 4, 6, 3, 7, 2, 5]
}
df3 = pd.DataFrame(data3)

# 1. 
avg_salary = df3.groupby("Department")["Salary"].mean()

# 2. 
most_experienced = df3.loc[df3["Experience (Years)"].idxmax()]

# 3. 
min_salary = df3["Salary"].min()
df3["Salary Increase (%)"] = ((df3["Salary"] - min_salary) / min_salary) * 100

# 4. 
df3["Department"].value_counts().plot(kind="bar", title="Employees per Department")
plt.ylabel("Number of Employees")
plt.show()

print("Average salary per department:\n", avg_salary, "\n")
print("Most experienced employee:\n", most_experienced, "\n")

# DataFrame 4: Customer Orders
data4 = {
    'Order_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Customer_ID': [201, 202, 203, 204, 205, 206, 207, 208, 209, 210],
    'Product': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'C', 'B', 'A'],
    'Quantity': [2, 3, 1, 4, 2, 3, 2, 5, 1, 3],
    'Total_Price': [120, 180, 60, 240, 160, 270, 140, 300, 90, 180]
}
df4 = pd.DataFrame(data4)

# 1. 
total_revenue = df4["Total_Price"].sum()

# 2.
most_ordered_product = df4["Product"].value_counts().idxmax()

# 3.
avg_quantity = df4["Quantity"].mean()

# 4. 
df4.groupby("Product")["Total_Price"].sum().plot(kind="pie", autopct="%1.1f%%", title="Sales Distribution by Product")
plt.ylabel("")
plt.show()

print("Total revenue:", total_revenue)
print("Most ordered product:", most_ordered_product)
print("Average quantity ordered:", avg_quantity)
