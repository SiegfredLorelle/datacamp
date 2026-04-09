"""Functions for initial exploration

You are researching unemployment rates worldwide and have been given a new dataset to work with. The data has been saved and loaded for you as a pandas DataFrame called unemployment. You've never seen the data before, so your first task is to use a few pandas functions to learn about this new data.

pandas has been imported for you as pd.
Instructions 1/3
        Use a pandas function to print the first five rows of the unemployment DataFrame.
Instructions 2/3
        Use a pandas function to print a summary of column non-missing values and data types from the unemployment DataFrame.
Instructions 3/3
        Print the summary statistics (count, mean, standard deviation, min, max, and quartile values) of each numerical column in unemployment.
"""

# Print the first five rows of unemployment
print(unemployment.head())


# Print a summary of non-missing values and data types in the unemployment DataFrame
print(unemployment.info())

# Print summary statistics for numerical columns in unemployment
print(unemployment.describe())


"""Counting categorical values
Recall from the previous exercise that the unemployment DataFrame contains 182 rows of country data including country_code, country_name, continent, and unemployment percentages from 2010 through 2021.
You'd now like to explore the categorical data contained in unemployment to understand the data that it contains related to each continent.

The unemployment DataFrame has been loaded for you along with pandas as pd.
Instructions
    Use a method to count the values associated with each continent in the unemployment
"""

# Count the values associated with each continent in unemployment
print(unemployment.value_counts("continent"))


"""Global unemployment in 2021

It's time to explore some of the numerical data in unemployment! What was typical unemployment in a given year? What was the minimum and maximum unemployment rate, and what did the distribution of the unemployment rates look like across the world? A histogram is a great way to get a sense of the answers to these questions.

Your task in this exercise is to create a histogram showing the distribution of global unemployment rates in 2021.

The unemployment DataFrame has been loaded for you along with pandas as pd.
Instructions
    Import the required visualization libraries.
    Create a histogram of the distribution of 2021 unemployment percentages across all countries in unemployment; show a full percentage point in each bin.
"""

# Import the required visualization libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Create a histogram of 2021 unemployment; show a full percent in each bin
sns.histplot(
    data=unemployment,
    x="2021",
    binwidth=1,
)
plt.show()


"""Detecting data types

A column has been changed in the unemployment DataFrame and it now has the wrong data type! This data type will stop you from performing effective exploration and analysis, so your task is to identify which column has the wrong data type and then fix it.

pandas has been imported as pd; unemployment is also available.
Instructions
    Update the data type of the 2019 column of unemployment to float.
    Print the dtypes of the unemployment DataFrame again to check that the data type has been updated!
"""

# Update the data type of the 2019 column to a float
unemployment["2019"] = unemployment["2019"].astype("float")
# Print the dtypes to check your work
print(unemployment.info())

"""Validating continents

Your colleague has informed you that the data on unemployment from countries in Oceania is not reliable, and you'd like to identify and exclude these countries from your unemployment data. The .isin() function can help with that!

Your task is to use .isin() to identify countries that are not in Oceania. These countries should return True while countries in Oceania should return False. This will set you up to use the results of .isin() to quickly filter out Oceania countries using Boolean indexing.

The unemployment DataFrame is available, and pandas has been imported as pd.
Instructions 1/2
    Define a Series of Booleans describing whether or not each continent is outside of Oceania; call this Series not_oceania.
Instructions 2/2
    Use Boolean indexing to print the unemployment DataFrame without any of the data related to countries in Oceania.
"""

# Define a Series describing whether each continent is outside of Oceania
not_oceania = ~unemployment["continent"].isin(["Oceania"])


# Define a Series describing whether each continent is outside of Oceania
not_oceania = ~unemployment["continent"].isin(["Oceania"])

# Print unemployment without records related to countries in Oceania
print(unemployment[not_oceania])



"""Validating range

Now it's time to validate our numerical data. We saw in the previous lesson using .describe() that the largest unemployment rate during 2021 was nearly 34 percent, while the lowest was just above zero.

Your task in this exercise is to get much more detailed information about the range of unemployment data using Seaborn's boxplot, and you'll also visualize the range of unemployment rates in each continent to understand geographical range differences.

unemployment is available, and the following have been imported for you: Seaborn as sns, matplotlib.pyplot as plt, and pandas as pd.
Instructions
    Print the minimum and maximum unemployment rates, in that order, during 2021.
    Create a boxplot of 2021 unemployment rates (on the x-axis), broken down by continent (on the y-axis).
"""

# Print the minimum and maximum unemployment rates during 2021
print(unemployment["2021"].min(), unemployment["2021"].max())

# Create a boxplot of 2021 unemployment rates, broken down by continent
sns.boxplot(
    data=unemployment,
    x="2021",
    y="continent"
)
plt.show()


"""Summaries with .groupby() and .agg()

In this exercise, you'll explore the means and standard deviations of the yearly unemployment data. First, you'll find means and standard deviations regardless of the continent to observe worldwide unemployment trends. Then, you'll check unemployment trends broken down by continent.

The unemployment DataFrame is available, and pandas has been imported as pd.
Instructions 1/2
        Print the mean and standard deviation of the unemployment rates for 2019 and 2020 (in that order).
    There was an error in your code
Instructions 2/2
        Print the mean and standard deviation (in that order) of the unemployment rates for 2019 and 2020, grouped by continent.
"""

# Print the mean and standard deviation of rates for 2019 and 2020 
print(unemployment[["2019", "2020"]].agg(["mean", "std"]))


# Print mean and standard deviation grouped by continent
print(
    unemployment[["continent", "2019", "2020"]]
    .groupby("continent")
    .agg(["mean", "std"])
)


"""Named aggregations

You've seen how .groupby() and .agg() can be combined to show summaries across categories. Sometimes, it's helpful to name new columns when aggregating so that it's clear in the code output what aggregations are being applied and where.

Your task is to create a DataFrame called continent_summary which shows a row for each continent. The DataFrame columns will contain the mean unemployment rate for each continent in 2021 as well as the standard deviation of the 2021 employment rate. And of course, you'll rename the columns so that their contents are clear!

The unemployment DataFrame is available, and pandas has been imported as pd.
Instructions
    Create a column called mean_rate_2021 which shows the mean 2021 unemployment rate for each continent.
    Create a column called std_rate_2021 which shows the standard deviation of the 2021 unemployment rate for each continent.
"""

continent_summary = unemployment.groupby("continent").agg(
    # Create the mean_rate_2021 column
    mean_rate_2021=("2021", "mean"),
    # Create the std_rate_2021 column
    std_rate_2021=("2021", "std"),
)
print(continent_summary)


"""Visualizing categorical summaries

As you've learned in this chapter, Seaborn has many great visualizations for exploration, including a bar plot for displaying an aggregated average value by category of data.

In Seaborn, bar plots include a vertical bar indicating the 95% confidence interval for the categorical mean. Since confidence intervals are calculated using both the number of values and the variability of those values, they give a helpful indication of how much data can be relied upon.

Your task is to create a bar plot to visualize the means and confidence intervals of unemployment rates across the different continents.

unemployment is available, and the following have been imported for you: Seaborn as sns, matplotlib.pyplot as plt, and pandas as pd.
Instructions
    Create a bar plot showing continents on the x-axis and their respective average 2021 unemployment rates on the y-axis.
"""

# Create a bar plot of continents and their average unemployment
sns.barplot(
    data=unemployment,
    x="continent",
    y="2021"
)
plt.show()


