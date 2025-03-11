import pandas as pd

# CSV file load with encoding fix
file_path = "sales_data_sample.csv"  # Ensure that the file is in the correct folder
df = pd.read_csv(file_path, encoding='latin1')

# to see first 5 rows
print(df.head())

# to understand the structure of data
print(df.info())

# to see columns names
print(df.columns)

# total rows and columns in dataset
print(df.shape)

# to check the missing values
print(df.isnull().sum())

# drop the Unnecessary columns
df.drop(columns=['ADDRESSLINE2', 'PHONE'], inplace=True)

#  fill the missing values of STATE, TERRITORY aur POSTALCODE
df['STATE'].fillna("Unknown", inplace=True)
df['TERRITORY'].fillna("Not Assigned", inplace=True)
df['POSTALCODE'].fillna("000000", inplace=True)

# Check missing values again
print(df.isnull().sum())


# Basic Statistics of Sales Data 
print("\n🔹 Basic Statistics of Sales Data:")
print(df[['SALES', 'QUANTITYORDERED', 'PRICEEACH']].describe())

# to get Year-wise total sales
yearly_sales = df.groupby('YEAR_ID')['SALES'].sum()
print("\n🔹 Yearly Total Sales:")
print(yearly_sales)

import matplotlib.pyplot as plt

# to get Country-wise total sales calculate 
country_sales = df.groupby('COUNTRY')['SALES'].sum().sort_values(ascending=False).head(10)

# to Graph plot
plt.figure(figsize=(10, 5))
plt.bar(country_sales.index, country_sales.values, color='m', alpha=0.7)

# Labels aur Title
plt.xlabel("Country")
plt.ylabel("Total Sales")
plt.title("Top 10 Countries by Sales")
plt.xticks(rotation=45)  # to tilt Country names
plt.grid(axis='y', linestyle='--', alpha=0.7)

# to Graph show
plt.show()


# calculate Month-wise total sales
monthly_sales = df.groupby('MONTH_ID')['SALES'].sum()

# to Graph plot
plt.figure(figsize=(8, 5))
plt.bar(monthly_sales.index, monthly_sales.values, color='g', alpha=0.7)

# Labels aur Title
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.title("Month-wise Sales Trend")
plt.xticks(range(1, 13))  # Months ko 1-12 dikhane ke liye
plt.grid(axis='y', linestyle='--', alpha=0.7)

# to Graph show
plt.show()

# to plot Sales Trends
plt.figure(figsize=(8, 5))
plt.plot(yearly_sales.index, yearly_sales.values, marker='o', linestyle='-', color='b', label="Total Sales")

# Labels aur Title
plt.xlabel("Year")
plt.ylabel("Total Sales")
plt.title("Year-wise Sales Trend")
plt.legend()
plt.grid()

# to Graph show 
plt.show()

# Product line-wise total sales
product_sales = df.groupby('PRODUCTLINE')['SALES'].sum().sort_values(ascending=False)

# to Graph plot
plt.figure(figsize=(10, 5))
plt.barh(product_sales.index, product_sales.values, color='c', alpha=0.7)

# Labels aur Title
plt.xlabel("Total Sales")
plt.ylabel("Product Line")
plt.title("Top-Selling Product Lines")
plt.grid(axis='x', linestyle='--', alpha=0.7)

# to Graph show 
plt.show()