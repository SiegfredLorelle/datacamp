""" Your first NumPy array
Once you're comfortable with NumPy, you'll find yourself converting Python lists into NumPy arrays all the time for increased speed and access to NumPy's excellent array methods.

sudoku_list is a Python list containing a sudoku game:

[[0, 0, 4, 3, 0, 0, 2, 0, 9],
 [0, 0, 5, 0, 0, 9, 0, 0, 1],
 [0, 7, 0, 0, 6, 0, 0, 4, 3],
 [0, 0, 6, 0, 0, 2, 0, 8, 7],
 [1, 9, 0, 0, 0, 7, 4, 0, 0],
 [0, 5, 0, 0, 8, 3, 0, 0, 0],
 [6, 0, 0, 0, 0, 0, 1, 0, 5],
 [0, 0, 3, 5, 0, 8, 6, 9, 0],
 [0, 4, 2, 9, 1, 0, 3, 0, 0]]
You're going to change sudoku_list into a NumPy array so you can practice with it in later lessons, for example by creating a 4D array of sudoku games along with their solutions!
"""
sudoku_list = [
    [0, 0, 4, 3, 0, 0, 2, 0, 9],
    [0, 0, 5, 0, 0, 9, 0, 0, 1],
    [0, 7, 0, 0, 6, 0, 0, 4, 3],
    [0, 0, 6, 0, 0, 2, 0, 8, 7],
    [1, 9, 0, 0, 0, 7, 4, 0, 0],
    [0, 5, 0, 0, 8, 3, 0, 0, 0],
    [6, 0, 0, 0, 0, 0, 1, 0, 5],
    [0, 0, 3, 5, 0, 8, 6, 9, 0],
    [0, 4, 2, 9, 1, 0, 3, 0, 0],
]

# Import NumPy
import numpy as np

# Convert sudoku_list into an array
sudoku_array = np.array(sudoku_list)

# Print the type of sudoku_array 
print(type(sudoku_array))



""" Creating arrays from scratch
It can be helpful to know how to create quick NumPy arrays from scratch in order to test your code. For example, when you are doing math with large multi-dimensional arrays, it's nice to check whether the math works as expected on small test arrays before applying your code to the larger arrays. NumPy has many options for creating smaller synthetic arrays.

With this in mind, it's time for you to create some arrays from scratch! numpy is imported for you as np.

Instructions 1/2
Create and print an array filled with zeros called zero_array, which has two rows and four columns.
Instructions 2/2
Create and print an array of random floats between 0 and 1 called random_array, which has three rows and six columns.
"""

# Create an array of zeros which has four columns and two rows
zero_array = np.zeros((2, 4))
print(zero_array)

# Create an array of random floats which has six columns and three rows
random_array = np.random.random((3, 6))
print(random_array)



""" A range array
np.arange() has especially useful applications in graphing. Your task is to create a scatter plot with the values from doubling_array on the y-axis.

doubling_array = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
Recall that a scatter plot can be created using the following code:

plt.scatter(x_values, y_values)
plt.show()
With doubling_array on the y-axis, you now need values for the x-axis, which you can create with np.arange()!

numpy is loaded for you as np, and matplotlib.pyplot is imported as plt.

Instructions
Using np.arange(), create a 1D array called one_to_ten which holds all integers from one to ten (inclusive).
Create a scatterplot with doubling_array as the y values and one_to_ten as the x values.
"""
import matplotlib.pyplot as plt
doubling_array = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]

# Create an array of integers from one to ten
one_to_ten = np.arange(1, 11)

# Create your scatterplot
plt.scatter(y=doubling_array, x=one_to_ten)
plt.show()



""" 3D array creation
In the first lesson, you created a sudoku_game two-dimensional NumPy array. Perhaps you have hundreds of sudoku game arrays, and you'd like to save the solution for this one, sudoku_solution, as part of the same array as its corresponding game in order to organize your sudoku data better. You could accomplish this by stacking the two 2D arrays on top of each other to create a 3D array.

numpy is loaded as np, and the sudoku_game and sudoku_solution arrays are available.

Instructions
Create a 3D array called game_and_solution by stacking the two 2D arrays, sudoku_game and sudoku_solution, on top of one another; in the final array, sudoku_game should appear before sudoku_solution.
Print game_and_solution.
"""

# Create the game_and_solution 3D array
game_and_solution = np.array(
    [
        sudoku_game,
        sudoku_solution,
    ]
)

# Print game_and_solution
print(game_and_solution) 



""" The fourth dimension
Printing arrays is a good way to check code output for small arrays like sudoku_game_and_solution, but it becomes unwieldy when dealing with bigger arrays and those with higher dimensions. Another important check is to look at the array's .shape.

Now, you'll create a 4D array that contains two sudoku games and their solutions. numpy is loaded as np. The game_and_solution 3D array you created in the previous example is available, along with new_sudoku_game and new_sudoku_solution.

Instructions
Create another 3D array called new_game_and_solution with a different 2D game and 2D solution pair: new_sudoku_game and new_sudoku_solution. new_sudoku_game should appear before new_sudoku_solution.
Create a 4D array called games_and_solutions by making an array out of the two 3D arrays: game_and_solution and new_game_and_solution, in that order.
Print the shape of games_and_solutions.
"""

# Create a second 3D array of another game and its solution 
new_game_and_solution = np.array(
    [
        new_sudoku_game,
        new_sudoku_solution,
    ]
)

# Create a 4D array of both game and solution 3D arrays
games_and_solutions = np.array(
    [
        game_and_solution,
        new_game_and_solution,
    ]
)

# Print the shape of your 4D array
print(games_and_solutions.shape)



""" Flattening and reshaping
You've learned to change not only array shape but also the number of dimensions that an array has. To test these skills, you'll change sudoku_game from a 2D array to a 1D array and back again. Can we trust NumPy to keep the array elements in the same order after being flattened and reshaped? Time to find out.

numpy is imported as np, and sudoku_game is loaded for you.

Instructions 1/2
Flatten sudoku_game so that it is a 1D array, and save it as flattened_game.
Print the .shape of flattened_game.
Instructions 2/2
Reshape the flattened_game back to its original shape of nine rows and nine columns; save the new array as reshaped_game.
"""

# Flatten sudoku_game
flattened_game = sudoku_game.flatten()

# Print the shape of flattened_game
print(flattened_game.shape)



# Flatten sudoku_game
flattened_game = sudoku_game.flatten()

# Print the shape of flattened_game
print(flattened_game.shape)

# Reshape flattened_game back to a nine by nine array
reshaped_game = flattened_game.reshape((9, 9))

# Print sudoku_game and reshaped_game
print(sudoku_game)
print(reshaped_game)



""" The dtype argument
One way to control the data type of a NumPy array is to declare it when the array is created using the dtype keyword argument. Take a look at the data type NumPy uses by default when creating an array with np.zeros(). Could it be updated?

numpy is loaded as np.

Instructions 1/2
Using np.zeros(), create an array of zeros that has three rows and two columns; call it zero_array.
Print the data type of zero_array.
Instructions 2/2
Create a new array of zeros called zero_int_array, which will also have three rows and two columns, but the data type should be np.int32.
Print the data type of zero_int_array.
"""

# Create an array of zeros with three rows and two columns
zero_array = np.zeros(shape=(3, 2))

# Print the data type of zero_array
print(zero_array.dtype)



# Create an array of zeros with three rows and two columns
zero_array = np.zeros((3, 2))

# Print the data type of zero_array
print(zero_array.dtype)

# Create a new array of int32 zeros with three rows and two columns
zero_int_array = zero_array.astype("int32")

# Print the data type of zero_int_array
print(zero_int_array.dtype)



""" A smaller sudoku game
NumPy data types, which emphasize speed, are more specific than Python data types, which emphasize flexibility. When working with large amounts of data in NumPy, it's good practice to check the data type and consider whether a smaller data type is large enough for your data, since smaller data types use less memory.

It's time to make your sudoku game more memory-efficient using your knowledge of data types! sudoku_game has been loaded for you as a NumPy array. numpy is imported as np.

Instructions 1/3
Print the data type of the elements in sudoku_game.
A smaller sudoku game
NumPy data types, which emphasize speed, are more specific than Python data types, which emphasize flexibility. When working with large amounts of data in NumPy, it's good practice to check the data type and consider whether a smaller data type is large enough for your data, since smaller data types use less memory.
It's time to make your sudoku game more memory-efficient using your knowledge of data types! sudoku_game has been loaded for you as a NumPy array. numpy is imported as np.
Instructions 3/3
Change the data type of sudoku_game to be int8, an 8-bit integer; name the new array small_sudoku_game.
Print the data type of small_sudoku_game to be sure that your change to int8 is reflected.
"""

# Print the data type of sudoku_game
print(sudoku_game.dtype)



# Print the data type of sudoku_game
print(sudoku_game.dtype)

# Change the data type of sudoku_game to int8
small_sudoku_game = sudoku_game.astype("int8")

# Print the data type of small_sudoku_game
print(small_sudoku_game.dtype)