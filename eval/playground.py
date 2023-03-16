import numpy as np

# Original array
arr = np.array([[0, 1], 
                [2, 3]])

# Custom order for the 1th axis (columns)
custom_order = np.array([1, 0])

# Reorder the array along the 1th axis (columns) using the custom order
reordered_arr = np.take_along_axis(arr, custom_order[np.newaxis, :], axis=1)

print("Original array:")
print(arr)
print("Reordered array:")
print(reordered_arr)