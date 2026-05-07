import numpy as np

# Input array from the user
array1 = np.array(list(map(int, input().split())))

# Searching
search_value = int(input("Value to search: "))
count_value = int(input("Value to count: "))
broadcast_value = int(input("Value to add: "))

# Find indices where value matches in array1
print(np.where(array1== search_value)[0])
# Count occurrences in array1
print(np.count_nonzero(array1==count_value))
# Broadcasting addition
print(array1+broadcast_value)
# Sort the first array
print(np.sort(array1))