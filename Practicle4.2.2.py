import pandas as pd

# Prompt the user for the file name
file_name = input()

# Load the data
df = pd.read_csv(file_name)

 # Find the product with the highest total quantity sold
best_product = df.groupby('Product')['Quantity'].sum().idxmax()
highest_quantity = df.groupby('Product')['Quantity'].sum().max()
# Display the result
print(f"Best selling product: {best_product}")
print(f"Total quantity sold: {highest_quantity}")
