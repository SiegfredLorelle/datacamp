""" Mean and median
In this chapter, you'll be working with the 2018 Food Carbon Footprint Index from nu3. The food_consumption dataset contains information about the kilograms of food consumed per person per year in each country in each food category (consumption) as well as information about the carbon footprint of that food category (co2_emissions) measured in kilograms of carbon dioxide, or CO2, per person per year in each country.

In this exercise, you'll compute measures of center to compare food consumption in the US and Belgium using your pandas and numpy skills.

pandas is imported as pd for you and food_consumption is pre-loaded.

Instructions 1/2
Import numpy with the alias np.
Create two DataFrames: one that holds the rows of food_consumption for 'Belgium' and another that holds rows for 'USA'. Call these be_consumption and usa_consumption.
Calculate the mean and median of kilograms of food consumed per person per year for both countries.
Instructions 2/2
Subset food_consumption for rows with data about Belgium and the USA.
Group the subsetted data by country and select only the consumption column.
Calculate the mean and median of the kilograms of food consumed per person per year in each country using .agg().
"""
# Import numpy with alias np
import numpy as np

# Filter for Belgium
be_consumption = food_consumption[food_consumption["country"] == "Belgium"]

# Filter for USA
usa_consumption = food_consumption[food_consumption["country"] == "USA"]

# Calculate mean and median consumption in Belgium
print(be_consumption["consumption"].mean())
print(be_consumption["consumption"].median())

# Calculate mean and median consumption in USA
print(usa_consumption["consumption"].mean())
print(usa_consumption["consumption"].median())



# Import numpy as np
import numpy as np

# Subset for Belgium and USA only
be_and_usa = food_consumption[(food_consumption["country"] == "Belgium") | (food_consumption["country"] == "USA")]

# Group by country, select consumption column, and compute mean and median
print(be_and_usa.groupby("country")["consumption"].agg([np.mean, np.median]))




""" Mean vs. median
In the video, you learned that the mean is the sum of all the data points divided by the total number of data points, and the median is the middle value of the dataset where 50% of the data is less than the median, and 50% of the data is greater than the median. In this exercise, you'll compare these two measures of center.

pandas is loaded as pd, numpy is loaded as np, and food_consumption is available.

Instructions 1/4
Import matplotlib.pyplot with the alias plt.
Subset food_consumption to get the rows where food_category is 'rice'.
Create a histogram of co2_emission for rice and show the plot.
Instructions 3/4
Use .agg() to calculate the mean and median of co2_emission for rice.
"""

# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt

# Subset for food_category equals rice
rice_consumption = food_consumption[food_consumption["food_category"] == "rice"]

# Histogram of co2_emission for rice and show plot
rice_consumption["co2_emission"].hist()
plt.show()



# Subset for food_category equals rice
rice_consumption = food_consumption[food_consumption['food_category'] == 'rice']

# Calculate mean and median of co2_emission with .agg()
print(rice_consumption["co2_emission"].agg([np.mean, np.median]))




""" Quartiles, quantiles, and quintiles
Quantiles are a great way of summarizing numerical data since they can be used to measure center and spread, as well as to get a sense of where a data point stands in relation to the rest of the data set. For example, you might want to give a discount to the 10% most active users on a website.

In this exercise, you'll calculate quartiles, quintiles, and deciles, which split up a dataset into 4, 5, and 10 pieces, respectively.

Both pandas as pd and numpy as np are loaded and food_consumption is available.

Instructions 1/3
Calculate the quartiles of the co2_emission column of food_consumption.
Instructions 2/3
Calculate the six quantiles that split up the data into 5 pieces (quintiles) of the co2_emission column of food_consumption.
Instructions 3/3
Calculate the eleven quantiles of co2_emission that split up the data into ten pieces (deciles).
"""

# Calculate the quartiles of co2_emission
print(np.quantile(food_consumption["co2_emission"], [0, 0.25, 0.5, 0.75, 1]))

# Calculate the quintiles of co2_emission
print(np.quantile(food_consumption["co2_emission"], np.linspace(0, 1, 6)))

# Calculate the deciles of co2_emission
print(np.quantile(food_consumption["co2_emission"], np.linspace(0, 1, 11)))




""" Variance and standard deviation
Variance and standard deviation are two of the most common ways to measure the spread of a variable, and you'll practice calculating these in this exercise. Spread is important since it can help inform expectations. For example, if a salesperson sells a mean of 20 products a day, but has a standard deviation of 10 products, there will probably be days where they sell 40 products, but also days where they only sell one or two. Information like this is important, especially when making predictions.

Both pandas as pd and numpy as np are loaded, and food_consumption is available.

Instructions
Calculate the variance and standard deviation of co2_emission for each food_category by grouping and aggregating.
Import matplotlib.pyplot with alias plt.
Create a histogram of co2_emission for the beef food_category and show the plot.
Create a histogram of co2_emission for the eggs food_category and show the plot.
"""


# Print variance and sd of co2_emission for each food_category
print(food_consumption.groupby("food_category")["co2_emission"].agg(["std", "var"]))

# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt

# Create histogram of co2_emission for food_category 'beef'
food_consumption[food_consumption["food_category"] == "beef"]["co2_emission"].hist()
# Show plot
plt.show()

# Create histogram of co2_emission for food_category 'eggs'
food_consumption[food_consumption["food_category"] == "eggs"]["co2_emission"].hist()
# Show plot
plt.show()



""" Finding outliers using IQR
Outliers can have big effects on statistics like mean, as well as statistics that rely on the mean, such as variance and standard deviation. Interquartile range, or IQR, is another way of measuring spread that's less influenced by outliers. IQR is also often used to find outliers. If a value is less than 
 or greater than 
, it's considered an outlier. In fact, this is how the lengths of the whiskers in a matplotlib box plot are calculated.

Diagram of a box plot showing median, quartiles, and outliers

In this exercise, you'll calculate IQR and use it to find some outliers. pandas as pd and numpy as np are loaded and food_consumption is available.

Instructions 1/4
Calculate the total co2_emission per country by grouping by country and taking the sum of co2_emission. Store the resulting DataFrame as emissions_by_country.
Instructions 2/4
Compute the first and third quartiles of emissions_by_country and store these as q1 and q3.
Calculate the interquartile range of emissions_by_country and store it as iqr.
Instructions 3/4
Calculate the lower and upper cutoffs for outliers of emissions_by_country, and store these as lower and upper.
Instructions 4/4
Subset emissions_by_country to get countries with a total emission greater than the upper cutoff or a total emission less than the lower cutoff.
"""

# Calculate total co2_emission per country: emissions_by_country
emissions_by_country = food_consumption.groupby("country")["co2_emission"].sum()

print(emissions_by_country)



# Calculate total co2_emission per country: emissions_by_country
emissions_by_country = food_consumption.groupby('country')['co2_emission'].sum()

# Compute the first and third quartiles and IQR of emissions_by_country
q1 = np.quantile(emissions_by_country, [0.25])
q3 = np.quantile(emissions_by_country, [0.75])
iqr = q3 - q1



# Calculate total co2_emission per country: emissions_by_country
emissions_by_country = food_consumption.groupby('country')['co2_emission'].sum()

# Compute the first and third quantiles and IQR of emissions_by_country
q1 = np.quantile(emissions_by_country, 0.25)
q3 = np.quantile(emissions_by_country, 0.75)
iqr = q3 - q1

# Calculate the lower and upper cutoffs for outliers
lower = q1 - (1.5 * iqr)
upper = q3 + (1.5 * iqr)



# Calculate total co2_emission per country: emissions_by_country
emissions_by_country = food_consumption.groupby('country')['co2_emission'].sum()

# Compute the first and third quantiles and IQR of emissions_by_country
q1 = np.quantile(emissions_by_country, 0.25)
q3 = np.quantile(emissions_by_country, 0.75)
iqr = q3 - q1

# Calculate the lower and upper cutoffs for outliers
lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr

# Subset emissions_by_country to find outliers
outliers = emissions_by_country[(emissions_by_country < lower) | (emissions_by_country > upper)]
print(outliers)