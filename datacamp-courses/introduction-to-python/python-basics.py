""" The Python Interface
Hit Run Code to run your first Python code with Datacamp and see the output!

Notice the script.py window; this is where you can type Python code to solve exercises. You can hit Run Code and Submit Answer as often as you want. If you're stuck, you can click Get Hint, and ultimately Get Solution.

You can also use the IPython Shell interactively by typing commands and hitting Enter. Here, your code will not be checked for correctness so it is a great way to experiment.


Instructions
Experiment in the IPython Shell; type 5 / 8, for example.
Add another line of code to script.py, print(7 + 10), to be checked for correctness.
Hit Submit Answer to execute the Python script and receive feedback.
"""

# Example, do not modify!
print(5 / 8)

# Print the sum of 7 and 10
print(7 + 10)



""" Any comments?
You can also add comments to your Python scripts. Comments are important to make sure that you and others can understand what your code is about and do not run as Python code.

They start with # tag. See the comment in the editor, # Division; now it's your turn to add a comment!

Instructions
Above the print(7 + 10), add the comment

# Addition

"""

# Division
print(5 / 8)

# Addition
print(7 + 10)



""" Python as a calculator
Python is perfectly suited to do basic calculations. It can do addition, subtraction, multiplication and division.

The code in the script gives some examples.

Now it's your turn to practice!

Instructions
Print the sum of 4 + 5.
Print the result of subtracting 5 from 5.
Multiply 3 by 5.
Divide 10 by 2.
"""

# Addition
print(4 + 5)

# Subtraction
print(5 - 5)

# Multiplication
print(3 * 5)

# Division
print(10 / 2)



"""Variable Assignment
In Python, a variable allows you to refer to a value with a name. To create a variable x with a value of 5, you use =, like this example:

x = 5
You can now use the name of this variable, x, instead of the actual value, 5.

Remember, = in Python means assignment, it doesn't test equality!

Instructions
Create a variable savings with the value of 100.
Check out this variable by typing print(savings) in the script. 
"""

# Create a variable savings
savings = 100

# Print out savings
print(savings)

""" Calculations with variables
You've now created a savings variable, so let's start saving!

Instead of calculating with the actual values, you can use variables instead. The savings variable you created in the previous exercise with a value of 100 is available to you.

How much money would you have saved four months from now, if you saved $10 each month?

Instructions
Create a variable monthly_savings, equal to 10 and num_months, equal to 4.
Multiply monthly_savings by num_months and save it to new_savings.
Add new_savings to savings, saving the sum as total_savings.
Print the value of total_savings.
"""
# Create the variables monthly_savings and num_months
monthly_savings = 10
num_months = 4

# Multiply monthly_savings and num_months
new_savings = monthly_savings * num_months

# Add new_savings to your savings
total_savings = savings + new_savings

# Print total_savings
print(total_savings)

""" Other variable types
In the previous exercise, you worked with the integer Python data type:

int, or integer: a number without a fractional part. savings, with the value 100, is an example of an integer.
Next to numerical data types, there are three other very common data types:

float, or floating point: a number that has both an integer and fractional part, separated by a point. 1.1, is an example of a float.
str, or string: a type to represent text. You can use single or double quotes to build a string.
bool, or boolean: a type to represent logical values. It can only be True or False (the capitalization is important!).

Instructions
Create a new float, half, with the value 0.5.
Create a new string, intro, with the value "Hello! How are you?".
Create a new boolean, is_good, with the value True.
"""

# Create a variable half
half = 0.5

# Create a variable intro
intro = "Hello! How are you?"

# Create a variable is_good
is_good = True

""" Operations with other types
Hugo mentioned that different types behave differently in Python.

When you sum two strings, for example, you'll get different behavior than when you sum two integers or two booleans.

In the script some variables with different types have already been created. It's up to you to use them.

Instructions
Calculate the product of monthly_savings and num_months. Store the result in year_savings.
What do you think the resulting type will be? Find out by printing out the type of year_savings.
Calculate the sum of intro and intro and store the result in a new variable doubleintro.
Print out doubleintro. Did you expect this?
"""

monthly_savings = 10
num_months = 12
intro = "Hello! How are you?"

# Calculate year_savings using monthly_savings and num_months
year_savings = monthly_savings * num_months

# Print the type of year_savings
print(type(year_savings))

# Assign sum of intro and intro to doubleintro
doubleintro = intro + intro

# Print out doubleintro
print(doubleintro)

"""
Type conversion
Using the + operator to paste together two strings can be very useful in building custom messages.

Suppose, for example, that you've calculated your savings want to summarize the results in a string.

To do this, you'll need to explicitly convert the types of your variables. More specifically, you'll need str(), to convert a value into a string. str(savings), for example, will convert the integer savings to a string.

Similar functions such as int(), float() and bool() will help you convert Python values into any type.

Instructions
Hit Run Code to run the code. Try to understand the error message.
Fix the code such that the printout runs without errors; use the function str() to convert the variables savings and total_savings to strings.
Convert the variable pi_string to a float and store this float as a new variable, pi_float.
"""

# Definition of savings and total_savings
savings = 100
total_savings = 150

# Fix the printout
print("I started with $" + str(savings) + " and now have $" + str(total_savings) + ". Awesome!")

# Definition of pi_string
pi_string = "3.1415926"

# Convert pi_string into float: pi_float
pi_float = float(pi_string)




