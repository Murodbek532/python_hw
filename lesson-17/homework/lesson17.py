import pandas as pd
import numpy as np

# Create DataFrame
data = {
    'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)

# 1. Rename column names
df = df.rename(columns={"First Name": "first_name", "Age": "age"})

# 2. Print first 3 rows
print("First 3 rows:\n", df.head(3))

# 3. Find mean age
print("\nMean age:", df["age"].mean())

# 4. Select and print only the 'first_name' and 'City' columns
print("\nName and City:\n", df[["first_name", "City"]])

# 5. Add new column 'Salary' with random salary values
df["Salary"] = np.random.randint(4000, 10000, size=len(df))
print("\nWith Salary column:\n", df)

# 6. Display summary statistics
print("\nSummary statistics:\n", df.describe(include="all"))


# Create DataFrame
sales_and_expenses = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr"],
    "Sales": [5000, 6000, 7500, 8000],
    "Expenses": [3000, 3500, 4000, 4500]
})

# 1. Maximum
print("\nMaximum Sales:", sales_and_expenses["Sales"].max())
print("Maximum Expenses:", sales_and_expenses["Expenses"].max())

# 2. Minimum
print("\nMinimum Sales:", sales_and_expenses["Sales"].min())
print("Minimum Expenses:", sales_and_expenses["Expenses"].min())

# 3. Average
print("\nAverage Sales:", sales_and_expenses["Sales"].mean())
print("Average Expenses:", sales_and_expenses["Expenses"].mean())

# Create DataFrame
expenses = pd.DataFrame({
    "Category": ["Rent", "Utilities", "Groceries", "Entertainment"],
    "January": [1200, 200, 300, 150],
    "February": [1300, 220, 320, 160],
    "March": [1400, 240, 330, 170],
    "April": [1500, 250, 350, 180]
})

# Set index
expenses = expenses.set_index("Category")

# 1. Maximum per category
print("\nMaximum expense per category:\n", expenses.max(axis=1))

# 2. Minimum per category
print("\nMinimum expense per category:\n", expenses.min(axis=1))

# 3. Average per category
print("\nAverage expense per category:\n", expenses.mean(axis=1))
