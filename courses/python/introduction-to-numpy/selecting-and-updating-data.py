""" Slicing and indexing trees
Imagine you are a researcher working with data from New York City's tree census. Each row of the tree_census 2D array lists information for a different tree: the tree ID, block ID, trunk diameter, and stump diameter in that order. Living trees do not have stump diameters, which explains why there are so many zeros in that column. Column order is important because NumPy does not have column names! The first and last three rows of tree_census are shown below.

array([[     3, 501451,     24,      0],
       [     4, 501451,     20,      0],
       [     7, 501911,      3,      0],
       ...,
       [  1198, 227387,     11,      0],
       [  1199, 227387,     11,      0],
       [  1210, 227386,      6,      0]])
In this exercise, you'll be working specifically with the second column, representing block IDs: your research requires you to select specific city blocks for further analysis using NumPy slicing and indexing. numpy is loaded as np, and the tree_census 2D array is available.

Instructions 1/3
Select all rows of data from the second column, representing block IDs; save the resulting array as block_ids.
Print the first five block IDs from block_ids.
Instructions 2/3
Select the tenth block ID from block_ids, saving the result as tenth_block_id.
Instructions 3/3
Select five consecutive block IDs from block_ids, starting with the tenth ID, and save as block_id_slice
"""

# Select all rows of block ID data from the second column
block_ids = tree_census[:, 1]

# Print the first five block_ids
print(block_ids[:5])



# Select all rows of block ID data from the second column
block_ids = tree_census[:, 1]

# Select the tenth block ID from block_ids
tenth_block_id = block_ids[10]
print(tenth_block_id)



# Select all rows of block ID data from the second column
block_ids = tree_census[:, 1]

# Select five block IDs from block_ids starting with the tenth ID
block_id_slice = block_ids[9: 14]
print(block_id_slice)



""" Stepping into 2D
Now assume that your research requires you to take an admittedly unrepresentative sample of trunk diameters, which are located in the third column of tree_census. Getting just a selection of trunk diameters can be done with NumPy's slicing and stepping functionality.

numpy is loaded as np, and the tree_census 2D array is available.

Instructions 1/2
Create an array called hundred_diameters which contains the first 100 trunk diameters in tree_census.
Instructions 2/2
Create an array,every_other_diameter, which contains only trunk diameters for trees with even row indices from 50 to 100, inclusive.
"""

# Create an array of the first 100 trunk diameters from tree_census
hundred_diameters = tree_census[:100, 2]
print(hundred_diameters)


# Create an array of trunk diameters with even row indices from 50 to 100 inclusive
every_other_diameter = tree_census[50:101:2, 2]
print(every_other_diameter)



""" Sorting trees
Sometimes it's easiest to understand data when it is sorted according to the value you are most interested in. Your new research task is to create an array containing the trunk diameters in the New York City tree census, sorted in order from smallest to largest.

numpy is loaded as np, and the tree_census 2D array is available.

Instructions
Create an array called sorted_trunk_diameters which selects only the trunk diameter column from tree_census and sorts it so that the smallest trunk diameters are at the top of the array and the largest at the bottom.
"""

# Extract trunk diameters information and sort from smallest to largest
sorted_trunk_diameters = np.sort(tree_census[:, 2])
print(sorted_trunk_diameters)




""" Filtering with masks
In the last lesson, you sorted trees from smallest to largest. Now, you'll use fancy indexing to return the row of data representing the largest tree in tree_census. You'll also examine other trees located on the same block as the largest tree: are they also large?

numpy is loaded as np, and the tree_census array is available. As a reminder, the tree_census columns in order refer to a tree's ID, its block ID, its trunk diameter, and its stump diameter.

Instructions 1/3
Using Boolean indexing, create an array, largest_tree_data, which contains the row of data on the largest tree in tree_census corresponding to the tree with a diameter of 51.
Instructions 2/3
Slice largest_tree_data to retrieve only the block id of the block the largest tree is located on; save this block id as largest_tree_block_id.
Instructions 3/3
Using fancy indexing, create an array called trees_on_largest_tree_block which contains data on all trees with the same block ID as the largest tree.
"""

# Create an array which contains row data on the largest tree in tree_census
largest_tree_data = tree_census[tree_census[:, 2] == 51]
print(largest_tree_data)



# Create an array which contains row data on the largest tree in tree_census
largest_tree_data = tree_census[tree_census[:, 2] == 51]
print(largest_tree_data)

# Slice largest_tree_data to get only the block id
largest_tree_block_id = largest_tree_data[:, 1]
print(largest_tree_block_id)



# Create an array which contains row data on the largest tree in tree_census
largest_tree_data = tree_census[tree_census[:, 2] == 51]
print(largest_tree_data)

# Slice largest_tree_data to get only the block ID
largest_tree_block_id = largest_tree_data[:, 1]
print(largest_tree_block_id)

# Create an array which contains row data on all trees with largest_tree_block_id
trees_on_largest_tree_block = tree_census[tree_census[:, 1] == largest_tree_block_id]
print(trees_on_largest_tree_block)




""" Fancy indexing vs. np.where()
You and your tree research team are double-checking collection data by visiting a few trees in person to confirm their measurements. You've been assigned to check the data for trees on block 313879, and you'd like to make a small array of just the tree data that relates to your work.

numpy is loaded as np, and the tree_census array is available. As a reminder, the tree_census columns in order refer to a tree's ID, its block ID, its trunk diameter, and its stump diameter.

Instructions 1/2
Using fancy indexing, create an array called block_313879 which only contains data for trees with a block ID of 313879.
Instructions 2/2
Using np.where(), create an array of row_indices for trees with a block ID of 313879.
Using row_indices, create block_313879, which contains data for trees on block 313879.
"""

# Create the block_313879 array containing trees on block 313879
block_313879 = tree_census[tree_census[:, 1] == 313879]
print(block_313879)


# Create an array of row_indices for trees on block 313879
row_indices = np.where(tree_census[:, 1] == 313879)

# Create an array which only contains data for trees on block 313879
block_313879 = tree_census[row_indices]
print(block_313879)



""" Creating arrays from conditions
Currently, the stump diameter and trunk diameter values in tree_census are in two different columns. Living trees have a stump diameter of zero while stumps have a trunk diameter of zero. If you'd like to include both living trees and stumps in certain research calculations, it might be useful to have their diameters together in just one column.

numpy is loaded as np, and the tree_census array is available. As a reminder, the tree census columns in order refer to a tree's ID, its block ID, its trunk diameter, and its stump diameter.

Instructions
Create and print a 1D array called trunk_stump_diameters, which replaces a tree's trunk diameter with its stump diameter if the trunk diameter is zero.
"""

# Create and print a 1D array of tree and stump diameters
trunk_stump_diameters = np.where(tree_census[:, 2] == 0, tree_census[:, 3], tree_census[:, 2])
print(trunk_stump_diameters)



""" Adding rows
The research team has discovered two trees that were left off the tree_census. Your task is to add rows containing the data for these new trees to the end of the tree_census array. The new trees' data is saved in a 2D array called new_trees:

new_trees = np.array([[1211, 227386, 20, 0], [1212, 227386, 8, 0]])
numpy is loaded as np, and the tree_census and new_trees arrays are available.

Instructions 1/2
Print the shapes of tree_census and new_trees to confirm they are compatible to concatenate.
Instructions 2/2
Add rows to the end of tree_census containing data for the new trees from the new_trees 2D array; save the new array as updated_tree_census.
"""

# Print the shapes of tree_census and new_trees
print(tree_census.shape, new_trees.shape)


# Print the shapes of tree_census and new_trees
print(tree_census.shape, new_trees.shape)

# Add rows to tree_census which contain data for the new trees
updated_tree_census = np.concatenate((tree_census, new_trees), axis=0)
print(updated_tree_census)



""" Adding columns
You finished the last set of exercises by creating an array called trunk_stump_diameters, which combined data from the trunk diameter and stump diameter columns into a 1D array. Now, you'll add that 1D array as a column to the tree_census array.

numpy is loaded as np, and both the tree_census and trunk_stump_diameters arrays are available.

Instructions 1/3
Print the shapes of both tree_census and trunk_stump_diameters.
Instructions 2/3
Reshape trunk_stump_diameters so that it can be appended as the last column in tree_census; call the reshaped array reshaped_diameters.
Instructions 3/3
Concatenate reshaped_diameters to the end of tree_census so that it becomes the last column; call the new array concatenated_tree_census.
"""

# Print the shapes of tree_census and trunk_stump_diameters
print(tree_census.shape, trunk_stump_diameters.shape)



# Print the shapes of tree_census and trunk_stump_diameters
print(trunk_stump_diameters.shape, tree_census.shape)

# Reshape trunk_stump_diameters
reshaped_diameters = trunk_stump_diameters.reshape((1000, 1))



# Print the shapes of tree_census and trunk_stump_diameters
print(trunk_stump_diameters.shape, tree_census.shape)

# Reshape trunk_stump_diameters
reshaped_diameters = trunk_stump_diameters.reshape((1000, 1))

# Concatenate reshaped_diameters to tree_census as the last column
concatenated_tree_census = np.concatenate((tree_census, reshaped_diameters), axis=1)
print(concatenated_tree_census)



""" Deleting with np.delete()
What if your tree research focuses only on living trees on publicly-owned city blocks? It might be helpful to delete some unneeded data like the stump diameter column and some trees located on private blocks.

You've learned that NumPy's np.delete() function takes three arguments: the original array, the index or indices to be deleted, and the axis to delete along. If you don't know the index or indices of the array you'd like to delete, recall that when it is only passed one argument,np.where() returns an array of indices where a condition is met!

numpy is loaded as np, and the tree_census 2D array is available. The columns in order refer to a tree's ID, block number, trunk diameter, and stump diameter.

Instructions 1/2
Delete the stump diameter column from tree_census, and save the new 2D array as tree_census_no_stumps.
Using np.where(), find the indices of any trees on block 313879, a private block. Save the indices in an array called private_block_indices.
Instructions 2/2
Using the indices you just found using np.where(), delete the rows for trees on block 313879 from tree_census_no_stumps, saving the new 2D array as tree_census_clean.
Print the shape of tree_census_clean.
"""

# Delete the stump diameter column from tree_census
tree_census_no_stumps = np.delete(tree_census, -1, axis=1)

# Save the indices of the trees on block 313879
private_block_indices = np.where(tree_census[:, 1] == 313879)



# Delete the stump diameter column from tree_census
tree_census_no_stumps = np.delete(tree_census, 3, axis=1)

# Save the indices of the trees on block 313879
private_block_indices = np.where(tree_census[:,1] == 313879)

# Delete the rows for trees on block 313879 from tree_census_no_stumps
tree_census_clean = np.delete(tree_census_no_stumps, private_block_indices, axis=0)

# Print the shape of tree_census_clean
print(tree_census_clean.shape)


