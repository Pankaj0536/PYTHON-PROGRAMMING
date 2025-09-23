# Converting tuples to lists and vice versa for modification

# Original tuple
tuple1 = (12, 56, 74, 22)

# Tuples are immutable, so we cannot directly change '74' to '90'

# Step 1: Convert tuple to list
list1 = list(tuple1)

# Step 2: Modify the element in the list
list1[2] = 90

# Step 3: Convert list back to tuple
tuple2 = tuple(list1)

# Display results
print("Original tuple:", tuple1)    # Before modification
print("Modified tuple:", tuple2)    # After modification

# output:
# Original tuple: (12, 56, 74, 22)
# Modified tuple: (12, 56, 90, 22)