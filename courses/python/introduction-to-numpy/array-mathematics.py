"""Sales totals
The dataset you'll be working with during this chapter is one year's sales data by month for three different industries. Each row in this monthly_sales array represents a month from January to December. The first column has monthly sales data for liquor stores, the second column has data for restaurants, and the last column tracks sales for department stores.

array([[ 4134, 23925,  8657],
       [ 4116, 23875,  9142],
       [ 4673, 27197, 10645],
       [ 4580, 25637, 10456],
       [ 5109, 27995, 11299],
       [ 5011, 27419, 10625],
       [ 5245, 27305, 10630],
       [ 5270, 27760, 11550],
       [ 4680, 24988,  9762],
       [ 4913, 25802, 10456],
       [ 5312, 25405, 13401],
       [ 6630, 27797, 18403]])
Your task is to create an array with all the information from monthly_sales as well as a fourth column which totals the monthly sales across industries for each month.

numpy is loaded for you as np, and the monthly_sales array is available.

Instructions 1/2
Create a 2D array which contains a single column of total monthly sales across industries; call it monthly_industry_sales.
Instructions 2/2
Concatenate monthly_industry_sales with monthly_sales into a new array called monthly_sales_with_total, with the monthly cross-industry sales information in the final column.
"""

# Create a 2D array of total monthly sales across industries
monthly_industry_sales = monthly_sales.sum(axis=1, keepdims=True)
print(monthly_industry_sales)


# Create a 2D array of total monthly sales across industries
monthly_industry_sales = monthly_sales.sum(axis=1, keepdims=True)
print(monthly_industry_sales)

# Add this column as the last column in monthly_sales
monthly_sales_with_total = np.concatenate((monthly_sales, monthly_industry_sales), axis=1)
print(monthly_sales_with_total)



""" Plotting averages
Perhaps you have a hunch that department stores see greater increased sales than average during the end of the year as people rush to buy gifts. You'd like to test this theory by comparing monthly department store sales to average sales across all three industries.

numpy is loaded for you as np, and the monthly_sales array is available. The monthly_sales columns in order refer to liquor store, restaurant, and department store sales.

Instructions 1/2
Create a 1D array called avg_monthly_sales, which contains an average sales amount for each month across the three industries.
Instructions 2/2
Plot an array of the numbers one through twelve (representing each month) on the x-axis and avg_monthly_sales on the y-axis.
Plot an array of the numbers one through twelve on the x-axis and the department store sales column of monthly_sales on the y-axis.
"""

# Create the 1D array avg_monthly_sales
avg_monthly_sales = monthly_sales.mean(axis=1)
print(avg_monthly_sales)


# Create the 1D array avg_monthly_sales
avg_monthly_sales = monthly_sales.mean(axis=1)
print(avg_monthly_sales)

# Plot avg_monthly_sales by month
plt.plot(np.arange(1, avg_monthly_sales.shape[0] + 1), avg_monthly_sales, label="Average sales across industries")

# Plot department store sales by month
plt.plot(np.arange(1, monthly_sales.shape[0] + 1), monthly_sales[:, 2], label="Department store sales")
plt.legend()
plt.show()



""" Cumulative sales
In the last exercise, you established that December is a big month for department stores. Are there other months where sales increase or decrease significantly?

Your task now is to look at monthly cumulative sales for each industry. The slope of the cumulative sales line will explain a lot about how steady sales are over time: a straight line will indicate steady growth, and changes in slope will indicate relative increases or decreases in sales.

numpy is loaded for you as np, and the monthly_sales array is available. The monthly_sales columns in order refer to liquor store, restaurant, and department store sales.

Instructions 1/2
Find cumulative monthly sales for each industry, saving this data in an array called cumulative_monthly_industry_sales.
Instructions 2/2
Plot each industry's cumulative sales by month as separate lines, with cumulative sales on the y-axis and month number on the x-axis.
"""

# Find cumulative monthly sales for each industry
cumulative_monthly_industry_sales = monthly_sales.cumsum(axis=0)
print(cumulative_monthly_industry_sales)


# Find cumulative monthly sales for each industry
cumulative_monthly_industry_sales = monthly_sales.cumsum(axis=0)
print(cumulative_monthly_industry_sales)

# Plot each industry's cumulative sales by month as separate lines
plt.plot(np.arange(1, 13), cumulative_monthly_industry_sales[:, 0], label="Liquor Stores")
plt.plot(np.arange(1, 13), cumulative_monthly_industry_sales[:, 1], label="Restaurants")
plt.plot(np.arange(1, 13), cumulative_monthly_industry_sales[:, 2], label="Department stores")
plt.legend()
plt.show()


""" Tax calculations
It's possible to use vectorized operations to calculate taxes for the liquor, restaurant, and department store industries! We'll simplify the tax calculation process here and assume that government collects 5% of all sales across these industries as tax revenue.

Your task is to calculate the tax owed by each industry related to each month's sales. numpy is loaded for you as np, and the monthly_sales array is available.

Instructions 1/2
Create an array called tax_collected which calculates tax collected by industry and month by multiplying each element in monthly_sales by 0.05.
Instructions 2/2
Create an array that keeps track of total_tax_and_revenue collected by each industry and month by adding each element in tax_collected with its corresponding element in monthly_sales.
"""

# Create an array of tax collected by industry and month
tax_collected = monthly_sales * 0.05
print(tax_collected)


# Create an array of tax collected by industry and month
tax_collected = monthly_sales * 0.05
print(tax_collected)

# Create an array of sales revenue plus tax collected by industry and month
total_tax_and_revenue = tax_collected + monthly_sales
print(total_tax_and_revenue)



""" Projecting sales
You'd like to be able to plan for next year's operations by projecting what sales will be, and you've gathered multipliers specific to each month and industry. These multipliers are saved in an array called monthly_industry_multipliers. For example, the multiplier at monthly_industry_multipliers[0, 0] of 0.98 means that the liquor store industry is projected to have 98% of this January's sales in January of next year.

array([[0.98, 1.02, 1.  ],
       [1.00, 1.01, 0.97],
       [1.06, 1.03, 0.98],
       [1.08, 1.01, 0.98],
       [1.08, 0.98, 0.98],
       [1.1 , 0.99, 0.99],
       [1.12, 1.01, 1.  ],
       [1.1 , 1.02, 1.  ],
       [1.11, 1.01, 1.01],
       [1.08, 0.99, 0.97],
       [1.09, 1.  , 1.02],
       [1.13, 1.03, 1.02]])
numpy is loaded for you as np, and the monthly_sales and monthly_industry_multipliers arrays are available. The monthly_sales columns in order refer to liquor store, restaurant, and department store sales.

Instructions 1/2
Create an array called projected_monthly_sales which contains projected sales for all three industries based on the multipliers you have gathered.
Instructions 2/2
Create a graph that plots two lines: current liquor store sales by month and projected liquor store sales by month; months will be represented by an array of the numbers one through twelve.
"""

# Create an array of monthly projected sales for all industries
projected_monthly_sales = (monthly_industry_multipliers * monthly_sales)
print(projected_monthly_sales)



# Create an array of monthly projected sales for all industries
projected_monthly_sales = monthly_sales * monthly_industry_multipliers
print(projected_monthly_sales)

# Graph current liquor store sales and projected liquor store sales by month
plt.plot(np.arange(1, 13), monthly_sales[:, 0], label="Current liquor store sales")
plt.plot(np.arange(1, 13), projected_monthly_sales[:, 0], label="Projected liquor store sales")
plt.legend()
plt.show()



""" Vectorizing .upper()
There are many situations where you might want to use Python methods and functions on array elements in NumPy. You can always write a for loop to do this, but vectorized operations are much faster and more efficient, so consider using np.vectorize()!

You've got an array called names which contains first and last names:

names = np.array([["Izzy", "Monica", "Marvin"],
                  ["Weber", "Patel", "Hernandez"]])
You'd like to use one of the Python methods you learned on DataCamp, .upper(), to make all the letters of every name in the array uppercase. As a reminder, .upper() is a string method, meaning that it must be called on an instance of a string: str.upper().

Your task is to vectorize this Python method. numpy is loaded for you as np, and the names array is available.

Instructions
Create a vectorized function called vectorized_upper from the Python .upper() string method.
Apply vectorized_upper() to the names array and save the resulting array as uppercase_names.
"""

# Vectorize the .upper() string method
vectorized_upper = np.vectorize(str.upper)

# Apply vectorized_upper to the names array
uppercase_names = vectorized_upper(names)
print(uppercase_names)


""" Broadcasting across columns
Recall that when broadcasting across columns, NumPy requires you to be explicit that it should broadcast a vertical array, and horizontal and vertical 1D arrays do not exist in NumPy. Instead, you must first create a 2D array to declare that you have vertical data. Then, NumPy creates a copy of this 2D vertical array for each column and applies the desired operation.

A Python list called monthly_growth_rate with len() of 12 is available. This list represents monthly year-over-year expected growth for the economy; your task is to use broadcasting to multiply this list by each column in the monthly_sales array. The monthly_sales array is loaded, along with numpy as np.

Instructions
Convert monthly_growth_rate, currently a Python list, into a one-dimensional NumPy array called monthly_growth_1D.
Reshape monthly_growth_1D so that it is broadcastable column-wise across monthly_sales; call the new array monthly_growth_2D.
Using broadcasting, multiply each column in monthly_sales by monthly_growth_2D.
"""

# Convert monthly_growth_rate into a NumPy array
monthly_growth_1D = np.array(monthly_growth_rate)

# Reshape monthly_growth_1D
monthly_growth_2D = monthly_growth_1D.reshape((12, 1))

# Multiply each column in monthly_sales by monthly_growth_2D
print(monthly_sales * monthly_growth_2D)



""" Broadcasting across rows
In the last set of exercises, you used monthly_industry_multipliers, to create sales predictions. Recall that monthly_industry_multipliers looks like this:

array([[0.98, 1.02, 1.  ],
       [1.00, 1.01, 0.97],
       [1.06, 1.03, 0.98],
       [1.08, 1.01, 0.98],
       [1.08, 0.98, 0.98],
       [1.1 , 0.99, 0.99],
       [1.12, 1.01, 1.  ],
       [1.1 , 1.02, 1.  ],
       [1.11, 1.01, 1.01],
       [1.08, 0.99, 0.97],
       [1.09, 1.  , 1.02],
       [1.13, 1.03, 1.02]])
Assume you're not comfortable being so specific with your estimates. Rather, you'd like to use monthly_industry_multipliers to find a single average multiplier for each industry. Then you'll use that multiplier to project next year's sales.

numpy is loaded for you as np, and the monthly_sales and monthly_industry_multipliers arrays are available. The monthly_sales columns in order refer to liquor store, restaurant, and department store sales.

Instructions 1/3
Find the mean sales projection multiplier for each industry; save in an array called mean_multipliers.
Instructions 2/3
Print the shapes of mean_multipliers and monthly_sales to ensure they are suitable for broadcasting.
Instructions 3/3
Multiply each monthly sales value by the mean multiplier you found for that industry; save in an array called projected_sales.
"""

# Find the mean sales projection multiplier for each industry
mean_multipliers = monthly_industry_multipliers.mean(axis=0)
print(mean_multipliers)


# Find the mean sales projection multiplier for each industry
mean_multipliers = monthly_industry_multipliers.mean(axis=0)
print(mean_multipliers)

# Print the shapes of mean_multipliers and monthly_sales
print(mean_multipliers.shape, monthly_sales.shape)


# Find the mean sales projection multiplier for each industry
mean_multipliers = monthly_industry_multipliers.mean(axis=0)
print(mean_multipliers)

# Print the shapes of mean_multipliers and monthly_sales
print(mean_multipliers.shape, monthly_sales.shape)

# Multiply each value by the multiplier for that industry
projected_sales = monthly_sales * mean_multipliers
print(projected_sales)