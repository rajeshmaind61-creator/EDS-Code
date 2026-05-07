import pandas as pd

# Prompt the user for the file name
file_name = input()

# Load the data
df = pd.read_csv(file_name)
city_sales = df.groupby('City')['Quantity'].sum().reset_index()
best_city_row = city_sales.loc[city_sales['Quantity'].idxmax()]
best_city = best_city_row['City']

# write the code..

# Display the result
print(f"City sold the most products: {best_city}")