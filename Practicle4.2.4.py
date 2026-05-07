import pandas as pd
from itertools import combinations
from collections import Counter

# Prompt user to input the file name
file_name = input()

# Read data from the specified CSV file
df = pd.read_csv(file_name)

grouped = df.groupby("Date")["Product"].apply(list)

pairs_counter = Counter()
for products in grouped:
	pairs = combinations(sorted(products), 2)
	pairs_counter.update(pairs)

max_frequency = max(pairs_counter.values())
most_common_pairs = [(pair, freq) for pair, freq in pairs_counter.items() if freq == max_frequency]
# Output the most frequent product pairs
for (product1, product2), frequency in most_common_pairs:
	print(f"{product1} and {product2}: {frequency} times")
# write the code


# Output the most frequent product pairs