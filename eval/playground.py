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

# >>> x = np.arange(5)
# >>> x[:, None]
# array([[0],
#        [1],
#        [2],
#        [3],
#        [4]])
# >>> x[None, :]
# array([[0, 1, 2, 3, 4]])
# >>> np.shape(x[None, :])
# (1, 5)
# >>> np.shape(x[:, None])
# (5, 1)
# >>> ord = np.array([ [1, 1, 0], [1, 0, 0] ])[:,:, None]
# >>> ord
# array([[[1],
#         [1],
#         [0]],

#        [[1],
#         [0],
#         [0]]])
# >>> ord = np.array([ [1, 1, 0], [1, 0, 0] ])[..., None]
# >>> ord
# array([[[1],
#         [1],
#         [0]],

#        [[1],
#         [0],
#         [0]]])
# >>> 

tpr = np.array([[[ True, False],
                 [ True,  True],
                 [False, False]],
                [[False,  True],
                 [False, False],
                 [False, False]]])

# Calculate the sum of True values along the deepest axis
sums = tpr.sum(axis=2)

# Calculate the indices that would sort the sums array
sort_indices = np.argsort(sums, axis=1)

print(sort_indices)

all_top_level = np.arange(tpr.shape[0])[:, None]
result = tpr[all_top_level, sort_indices]

print(result)