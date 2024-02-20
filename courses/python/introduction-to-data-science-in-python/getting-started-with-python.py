""" Importing Python modules
Modules (sometimes called packages or libraries) help group together related sets of tools in Python. In this exercise, we'll examine two modules that are frequently used by Data Scientists:

statsmodels: used in machine learning; usually aliased as sm
seaborn: a visualization library; usually aliased as sns
Note that each module has a standard alias, which allows you to access the tools inside of the module without typing as many characters. For example, aliasing lets us shorten seaborn.scatterplot() to sns.scatterplot().

Instructions 1/3
In the script editor, use an import statement to import statsmodels without an alias.
Instructions 2/3
Add an as statement to alias statsmodels to sm.
Instructions 3/3
Add an as statement to alias seaborn to sns.
"""

# Use an import statement to import statsmodels
import statsmodels

# Import statsmodels under the alias sm
import statsmodels as sm

# Use an import statement to import seaborn with alias sns
import seaborn as sns



""" Correcting a broken import
In this exercise, we'll learn to import numpy, a module for performing mathematical operations on lists of data. The standard alias for numpy is np.

What did you need to change to make the import run without errors?

Fix the import of numpy to run without errors.
"""

# Fix the import of numpy to run without errors
import numpy as np




""" Creating a float
Before we start looking for Bayes' kidnapper, we need to fill out a Missing Puppy Report with details of the case. Each piece of information will be stored as a variable.

We define a variable using an equals sign (=). For instance, we would define the variable height:

height = 24
In this exercise, we'll be defining bayes_age to be 4.0 months old. The data type for this variable will be float, meaning that it is a number.

Instructions
Define a variable called bayes_age and set it equal to 4.0.
Display the variable bayes_age.
"""

# Fill in Bayes' age (4.0)
bayes_age = 4.0

# Display the variable bayes_age
print(bayes_age)




""" Creating strings
Let's continue to fill out the Missing Puppy Report for Bayes. In the previous exercise, we defined bayes_age, which was a float, which represents a number.

In this exercise, we'll define favorite_toy and owner, which will both be strings. A string represents text. A string is surrounded by quotation marks (' or ") and can contain letters, numbers, and special characters. It doesn't matter if you use single (') or double (") quotes, but it's important to be consistent throughout your code.

Instructions
Define a variable called favorite_toy whose value is "Mr. Squeaky".
Define a variable called owner whose value is 'DataCamp'.
Show the values assigned to these variables.
"""

# Bayes' favorite toy
favorite_toy = "Mr. Squeaky"

# Bayes' owner
owner = 'DataCamp'

# Display variables
print(favorite_toy)
print(owner)




""" Correcting string errors
It's easy to make errors when you're trying to type strings quickly.

Don't forget to use quotes! Without quotes, you'll get a name error.
owner = DataCamp
Use the same type of quotation mark. If you start with a single quote, and end with a double quote, you'll get a syntax error.
fur_color = "blonde'
Someone at the police station made an error when filling out the final lines of Bayes' Missing Puppy Report. In this exercise, you will correct the errors.

Instructions
Correct the mistakes in the code so that it runs without producing syntax errors.
"""

# One or more of the following lines contains an error
# Correct it so that it runs without producing syntax errors
birthday = "2017-07-14"
case_id = 'DATACAMP!123-456?'



""" Load a DataFrame
A ransom note was left at the scene of Bayes' kidnapping. Eventually, we'll want to analyze the frequency with which each letter occurs in the note, to help us identify the kidnapper. For now, we just need to load the data from ransom.csv into Python.

We'll load the data into a DataFrame, a special data type from the pandas module. It represents spreadsheet-like data (something with rows and columns).

We can create a DataFrame from a CSV (comma-separated value) file by using the function pd.read_csv().

Instructions
Use pd.read_csv() to load data from a CSV file called ransom.csv. This file represents the frequency of each letter in the ransom note for Bayes.
"""

# Import pandas
import pandas as pd

# Load the 'ransom.csv' into a DataFrame
r = pd.read_csv('ransom.csv')

# Display DataFrame
print(r)



""" Correcting a function error
The code in the script editor should plot information from the DataFrame that we loaded in the previous exercise.

However, there is an error in function syntax. Remember that common function errors include:

Forgetting closing parenthesis
Forgetting commas between each argument
Note that all arguments to the functions are correct. The problem is in the function syntax.

Instructions
Correct the code so that it runs without syntax errors.
"""

# One or more of the following lines contains an error
# Correct it so that it runs without producing syntax errors

# Plot a graph
plt.plot(x_values, y_values)

# Display the graph
plt.show()



""" Snooping for suspects
We need to narrow down the list of suspects for the kidnapping of Bayes. Once we have a list of suspects, we'll ask them for writing samples and compare them to the ransom note.

A witness to the crime noticed a green truck leaving the scene of the crime whose license plate began with 'FRQ'. We'll use this information to search for some suspects.

As a detective, you have access to a special function called lookup_plate.

lookup_plate accepts one positional argument: A string representing a license plate.

Instructions 1/3
Create a variable called plate that represents the observed license plate: the first three letters were FRQ, but the witness couldn't see the final 4 letters. Use asterisks (*) to represent missing letters.
Instructions 2/3
Call lookup_plate() using the variable plate.
Instructions 3/3
Calling lookup_plate() with the license plate FRQ**** produced too many results. Luckily, lookup_plate() also accepts a keyword argument: color. Use the color of the car ('Green') to get a smaller list.
"""

# Define plate to represent a plate beginning with FRQ
# Use * to represent the missing four letters
plate = 'FRQ****'

# Call the function lookup_plate()
lookup_plate(plate)

# Call lookup_plate() with the keyword argument for color
lookup_plate(plate, color="Green")


