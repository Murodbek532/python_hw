import pandas as pd

# Homework Assignment 1: Analyzing Sales Data

sales = pd.read_csv("task/sales_data.csv")

# 1. 
category_stats = sales.groupby("Category").agg(
    total_quantity=("Quantity", "sum"),
    avg_price=("Price", "mean"),
    max_quantity=("Quantity", "max")
).reset_index()

# 2. 
top_products = sales.groupby(["Category", "Product"])["Quantity"].sum().reset_index()
top_products = top_products.loc[top_products.groupby("Category")["Quantity"].idxmax()]

# 3. 
sales["Total"] = sales["Quantity"] * sales["Price"]
date_max_sales = sales.groupby("Date")["Total"].sum().idxmax()



# Homework Assignment 2: Examining Customer Orders

orders = pd.read_csv("task/customer_orders.csv")

# 1. 
orders_per_customer = orders.groupby("CustomerID")["OrderID"].nunique()
customers_20plus = orders_per_customer[orders_per_customer >= 20].index
filtered_customers = orders[orders["CustomerID"].isin(customers_20plus)]

# 2. 
avg_price_per_customer = orders.groupby("CustomerID")["Price"].mean()
customers_above_120 = avg_price_per_customer[avg_price_per_customer > 120].index

# 3. 
product_totals = orders.groupby("Product").agg(
    total_quantity=("Quantity", "sum"),
    total_price=("Price", "sum")
).reset_index()

filtered_products = product_totals[product_totals["total_quantity"] >= 5]



# Homework Assignment 3: Population Salary Analysis

import sqlite3
import pandas as pd
import numpy as np

# 1. 
conn = sqlite3.connect("task/population.db")
population = pd.read_sql("SELECT * FROM population", conn)
conn.close()

# 2. 
salary_bands = pd.read_excel("task/population salary analysis.xlsx")

# 3. 
def assign_band(salary):
    row = salary_bands[(salary_bands["MinSalary"] <= salary) & (salary <= salary_bands["MaxSalary"])]
    if not row.empty:
        return row["Band"].values[0]
    return "Other"

population["SalaryBand"] = population["Salary"].apply(assign_band)

# 4. 
salary_stats = population.groupby("SalaryBand").agg(
    percentage=("Salary", lambda x: len(x) / len(population) * 100),
    avg_salary=("Salary", "mean"),
    median_salary=("Salary", "median"),
    count=("Salary", "count")
).reset_index()

# 5. 
salary_stats_state = population.groupby(["State", "SalaryBand"]).agg(
    percentage=("Salary", lambda x: len(x) / len(population) * 100),
    avg_salary=("Salary", "mean"),
    median_salary=("Salary", "median"),
    count=("Salary", "count")
).reset_index()

