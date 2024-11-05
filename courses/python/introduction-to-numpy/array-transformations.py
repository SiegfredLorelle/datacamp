""" Loading .npy files
The exercises for this chapter will use a NumPy array holding an image in RGB format. Which image? You'll have to load the array from the mystery_image.npy file to find out!

numpy is loaded as np, and mystery_image.npy is available.

Instructions
Load the mystery_image.npy file using the alias f, saving the contents as an array called rgb_array.
"""

# Load the mystery_image.npy file 
with open("mystery_image.npy", "rb") as file:
    rgb_array = np.load(file)

plt.imshow(rgb_array)
plt.show()



""" Getting help
You'll need to use the .astype() array method we covered in the first chapter of this course for the next exercise. If you forget exactly how .astype() works, you could check out the course slides or NumPy's documentation on numpy.org. There is, however, an even faster way to jog your memory…

numpy is loaded as np.

Instructions
Return NumPy's documentation text for .astype().
"""

# Display the documentation for .astype()
help(np.ndarray.astype)



""" Update and save
Perhaps you are training a machine learning model to recognize ocean scenes. You'd like the model to understand that oceans are not only associated with bright, summery colors, so you're careful to include images of oceans in bad weather or evening light as well. You may have to manually transform some images in order to balance the data, so your task is to darken the Monet ocean scene rgb_array.

Recall from the video that white is associated with the maximum RGB value of 255, while darker colors are associated with lower values. numpy is loaded as np, and the 3D Monet rgb_array that you loaded in the last exercise is available.

Instructions 1/3
Reduce every value in rgb_array by 50 percent, saving the resulting array as darker_rgb_array.
Instructions 2/3
Since RGB values must be integers, convert darker_rgb_array into an array of integers called darker_rgb_int_array so that it can be plotted.
Instructions 3/3
Save darker_rgb_int_array as an .npy file called darker_monet.npy using the alias f.
"""

# Reduce every value in rgb_array by 50 percent
darker_rgb_array = rgb_array / 2


# Reduce every value in rgb_array by 50 percent
darker_rgb_array = rgb_array * 0.5

# Convert darker_rgb_array into an array of integers
darker_rgb_int_array = darker_rgb_array.astype("int8")
plt.imshow(darker_rgb_int_array)
plt.show()


# Reduce every value in rgb_array by 50 percent
darker_rgb_array = rgb_array * 0.5

# Convert darker_rgb_array into an array of integers
darker_rgb_int_array = darker_rgb_array.astype(np.int8)
plt.imshow(darker_rgb_int_array)
plt.show()

# Save darker_rgb_int_array to an .npy file called darker_monet.npy
with open("darker_monet.npy", "wb") as f:
    np.save(f, darker_rgb_int_array)



""" Augmenting Monet
Perhaps you're still working on that machine learning model that identifies ocean scenes in paintings. You'd like to generate a few extra images to augment your existing data. After all, a human can tell that a painting is of an ocean even if the painting is upside-down: why shouldn't your machine learning model?

numpy is loaded as np, and the 3D Monet rgb_array is available.

Instructions 1/2
Flip rgb_array so that it is the mirror image of the original, with the ocean on the right and grassy knoll on the left.
Instructions 2/2
Flip rgb_array so that it is upside down but otherwise remains the same.
"""


# Flip rgb_array so that it is the mirror image of the original
mirrored_monet = np.flip(rgb_array, axis=1)
plt.imshow(mirrored_monet)
plt.show()


# Flip rgb_array so that it is upside down
upside_down_monet = np.flip(rgb_array, axis=(0, 1))
plt.imshow(upside_down_monet)
plt.show()


""" Transposing your masterpiece
You've learned that transposing an array reverses the order of the array's axes. To transpose the axes in a different order, you can pass the desired axes order as arguments. You'll practice with the 3D Monet rgb_array, loaded for you. numpy has been imported as np.

Instructions
Transpose the 3-D rgb_array so that the image appears rotated 90 degrees left and as a mirror image of itself.
"""

# Transpose rgb_array
transposed_rgb = np.transpose(rgb_array, axes=(1, 0, 2))
plt.imshow(transposed_rgb)
plt.show()



""" 2D split and stack
Splitting and stacking skills aren't just useful with 3D RGB arrays: they are excellent for subsetting and organizing data of any type and dimension!

You'll now take a quick trip down memory lane to reorganize the monthly_sales array as a 3D array. Recall that the first dimension of monthly_sales is rows of a single month's sales across three industries, and the second dimension is columns of monthly sales data for a single industry.

Your task is to split this data into quarterly sales data and stack the quarterly sales data so that the new third dimension represents the four 2D arrays of quarterly sales.numpy is loaded as np, and the monthly_sales array is available.

Instructions 1/2
Split monthly_sales into four arrays representing quarterly data across industries; print q1_sales.
Instructions 2/2
Stack the four quarterly sales arrays to create a 3D array, quarterly_sales, made up of the four quarterly 2D arrays in order from the first to last quarter.
"""

# Split monthly_sales into quarterly data
q1_sales, q2_sales, q3_sales, q4_sales = np.split(monthly_sales, 4)
print(q1_sales)


# Split monthly_sales into quarterly data
q1_sales, q2_sales, q3_sales, q4_sales = np.split(monthly_sales, 4)

# Print q1_sales
print(q1_sales)

# Stack the four quarterly sales arrays
quarterly_sales = np.stack([q1_sales, q2_sales, q3_sales, q4_sales])
print(quarterly_sales)



""" Splitting RGB data
Perhaps you'd like to better understand Monet's use of the color blue. Your task is to create a version of the Monet rgb_array that emphasizes parts of the painting that use lots of blue by making them even bluer! You'll perform the splitting portion of this task in this exercise and the stacking portion in the next.

numpy is loaded as np, and the Monet rgb_array is available.

Instructions 1/3
Split the Monet rgb_array into red, green, and blue only pixel data; save the results as as red_array, green_array, and blue_array.
Instructions 2/3
Create emphasized_blue_array, which replaces blue_array values with 255 if they are higher than the mean value of blue_array; otherwise, the value remains the same.
Print the .shape of emphasized_blue_array.
Instructions 3/3
Reshape emphasized_blue_array to remove the trailing third dimension; save as emphasized_blue_array_2D.
"""

# Split rgb_array into red, green, and blue arrays
red_array, green_array, blue_array = np.split(rgb_array, 3, axis=2)



# Split rgb_array into red, green, and blue arrays
red_array, green_array, blue_array = np.split(rgb_array, 3, axis=2)

# Create emphasized_blue_array
emphasized_blue_array = np.where(blue_array > blue_array.mean(), 255, blue_array)

# Print the shape of emphasized_blue_array
print(emphasized_blue_array.shape)




# Split rgb_array into red, green, and blue arrays
red_array, green_array, blue_array = np.split(rgb_array, 3, axis=2)

# Create emphasized_blue_array
emphasized_blue_array = np.where(blue_array > blue_array.mean(), 255, blue_array)

# Print the shape of emphasized_blue_array
print(emphasized_blue_array.shape)

# Remove the trailing dimension from emphasized_blue_array
emphasized_blue_array_2D = emphasized_blue_array.reshape((675, 844))



""" Stacking RGB data
Now you'll combine red_array, green_array, and emphasized_blue_array_2D to see what Monet's painting looks like with the blues emphasized!

numpy is loaded as np, and the red_array, green_array, blue_array and emphasized_blue_array_2D objects that you created in the last exercise are available.

Instructions 1/3
Print the shapes of blue_array and emphasized_blue_array_2D.
Instructions 2/3
Reshape red_array and green_array so that they can be stacked with emphasized_blue_array_2D.
Instructions 3/3
Stack red_array_2D, green_array_2D, and emphasized_blue_array_2D together (in that order) into a 3D array called emphasized_blue_monet.
"""

# Print the shapes of blue_array and emphasized_blue_array_2D
print(blue_array.shape, emphasized_blue_array_2D.shape)



# Print the shapes of blue_array and emphasized_blue_array_2D
print(blue_array.shape, emphasized_blue_array_2D.shape)

# Reshape red_array and green_array
red_array_2D = red_array.reshape(675, 844)
green_array_2D = green_array.reshape(675, 844)



# Print the shapes of blue_array and emphasized_blue_array_2D
print(blue_array.shape, emphasized_blue_array_2D.shape)

# Reshape red_array and green_array
red_array_2D = red_array.reshape((675, 844))
green_array_2D = green_array.reshape((675, 844))

# Stack red_array_2D, green_array_2D, and emphasized_blue_array_2D
emphasized_blue_monet = np.stack([red_array_2D, green_array_2D, emphasized_blue_array_2D], axis=2)
plt.imshow(emphasized_blue_monet)
plt.show()