import pandas as pd
import matplotlib.pyplot as plt
# Load dataset
data = pd.read_csv(r"C:\Users\sakshi\OneDrive\Documents\python\intershipProject\sales_data.csv")

# Convert Date column to datetime
data["Date"] = pd.to_datetime(data["Date"])

# Create a new column: Total Sales
data["Total_Sales"] = data["Quantity"] * data["Price"]

# Display first few rows
print("Dataset Preview:\n", data.head())

# 1. Total Sales
total_sales = data["Total_Sales"].sum()
print("\nTotal Sales:", total_sales)

# 2. Sales by Product
sales_by_product = data.groupby("Product")["Total_Sales"].sum()
print("\nSales by Product:\n", sales_by_product)

# 3. Sales by Category
sales_by_category = data.groupby("Category")["Total_Sales"].sum()
print("\nSales by Category:\n", sales_by_category)

# 4. Monthly Sales Analysis
data["Month"] = data["Date"].dt.month
monthly_sales = data.groupby("Month")["Total_Sales"].sum()
print("\nMonthly Sales:\n", monthly_sales)

# Visualization

# 1. Bar Chart - Sales by Product
sales_by_product.plot(kind="bar", title="Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.show()

# 2. Pie Chart - Sales by Category
sales_by_category.plot(kind="pie", autopct="%1.1f%%", title="Sales by Category")
plt.ylabel("")
plt.show()

# 3. Line Chart - Monthly Sales Trend
monthly_sales.plot(kind="line", marker='o', title="Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.show()




