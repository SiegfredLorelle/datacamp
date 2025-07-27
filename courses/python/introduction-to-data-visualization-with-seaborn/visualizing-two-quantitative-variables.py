"""Creating subplots with col and row
We've seen in prior exercises that students with more absences ("absences") tend to have lower final grades ("G3"). Does this relationship hold regardless of how much time students study each week?
To answer this, we'll look at the relationship between the number of absences that a student has in school and their final grade in the course, creating separate subplots based on each student's weekly study time ("study_time").
Seaborn has been imported as sns and matplotlib.pyplot has been imported as plt.
Instructions 1/3
    Modify the code to use relplot() instead of scatterplot().
Instructions 2/3
Modify the code to create one scatter plot for each level of the variable "study_time", arranged in columns.
Instructions 3/3
Adapt your code to create one scatter plot for each level of a student's weekly study time, this time arranged in rows.
"""

# Change to use relplot() instead of scatterplot()
sns.relplot(x="absences", y="G3", 
                data=student_data, kind="scatter")

# Show plot
plt.show()


# Change to make subplots based on study time
sns.relplot(x="absences", y="G3", 
            data=student_data,
            col="study_time",
            kind="scatter")

# Show plot
plt.show()



# Change this scatter plot to arrange the plots in rows instead of columns
sns.relplot(x="absences", y="G3", 
            data=student_data,
            kind="scatter", 
            row="study_time")

# Show plot
plt.show()


"""Creating two-factor subplots
Let's continue looking at the student_data dataset of students in secondary school. Here, we want to answer the following question: does a student's first semester grade ("G1") tend to correlate with their final grade ("G3")?
There are many aspects of a student's life that could result in a higher or lower final grade in the class. For example, some students receive extra educational support from their school ("schoolsup") or from their family ("famsup"), which could result in higher grades. Let's try to control for these two factors by creating subplots based on whether the student received extra educational support from their school or family.
Seaborn has been imported as sns and matplotlib.pyplot has been imported as plt.
Instructions 1/3
Use relplot() to create a scatter plot with "G1" on the x-axis and "G3" on the y-axis, using the student_data DataFrame.
Instructions 1/3
Create column subplots based on whether the student received support from the school ("schoolsup"), ordered so that "yes" comes before "no".
Instructions 1/3
Add row subplots based on whether the student received support from the family ("famsup"), ordered so that "yes" comes before "no". This will result in subplots based on two factors.
"""

# Create a scatter plot of G1 vs. G3
sns.relplot(
    kind="scatter",
    x="G1",
    y="G3",
    data=student_data
)

# Show plot
plt.show()


# Adjust to add subplots based on school support
sns.relplot(x="G1", y="G3", 
            data=student_data,
            kind="scatter",
            col="schoolsup",
            col_order=[
                "yes",
                "no"
            ])

# Show plot
plt.show()


# Adjust further to add subplots based on family support
sns.relplot(x="G1", y="G3", 
            data=student_data,
            kind="scatter", 
            col="schoolsup",
            col_order=["yes", "no"],
            row="famsup",
            row_order=["yes", "no"])

# Show plot
plt.show()


"""Changing the size of scatter plot points
In this exercise, we'll explore Seaborn's mpg dataset, which contains one row per car model and includes information such as the year the car was made, the number of miles per gallon ("M.P.G.") it achieves, the power of its engine (measured in "horsepower"), and its country of origin.
What is the relationship between the power of a car's engine ("horsepower") and its fuel efficiency ("mpg")? And how does this relationship vary by the number of cylinders ("cylinders") the car has? Let's find out.
Let's continue to use relplot() instead of scatterplot() since it offers more flexibility.
Instructions 1/2
Use relplot() and the mpg DataFrame to create a scatter plot with "horsepower" on the x-axis and "mpg" on the y-axis. Vary the size of the points by the number of cylinders in the car ("cylinders").
Instructions 2/2
To make this plot easier to read, use hue to vary the color of the points by the number of cylinders in the car ("cylinders").
"""
# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create scatter plot of horsepower vs. mpg
sns.relplot(
    kind="scatter",
    data=mpg,
    x="horsepower",
    y="mpg",
    size="cylinders"
)

# Show plot
plt.show()



# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create scatter plot of horsepower vs. mpg
sns.relplot(x="horsepower", y="mpg", 
            data=mpg, kind="scatter", 
            size="cylinders",
            hue="cylinders",
)

# Show plot
plt.show()


# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create a scatter plot of acceleration vs. mpg
sns.relplot(
    kind="scatter",
    data=mpg,
    x="acceleration",
    y="mpg",
    hue="origin",
    style="origin"
)

# Show plot
plt.show()


"""Interpreting line plots
In this exercise, we'll continue to explore Seaborn's mpg dataset, which contains one row per car model and includes information such as the year the car was made, its fuel efficiency (measured in "miles per gallon" or "M.P.G"), and its country of origin (USA, Europe, or Japan).
How has the average miles per gallon achieved by these cars changed over time? Let's use line plots to find out!
Instructions
Use relplot() and the mpg DataFrame to create a line plot with "model_year" on the x-axis and "mpg" on the y-axis.
"""

# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create line plot
sns.relplot(
    kind="line",
    data=mpg,
    x="model_year",
    y="mpg",
)

# Show plot
plt.show()


"""Visualizing standard deviation with line plots
In the last exercise, we looked at how the average miles per gallon achieved by cars has changed over time. Now let's use a line plot to visualize how the distribution of miles per gallon has changed over time.
Seaborn has been imported as sns and matplotlib.pyplot has been imported as plt.
Instructions
Change the plot so the shaded area shows the standard deviation instead of the confidence interval for the mean.
"""
# Make the shaded area show the standard deviation
sns.relplot(x="model_year", y="mpg",
            data=mpg, kind="line",
            ci="sd")

# Show plot
plt.show()

"""Plotting subgroups in line plots

Let's continue to look at the mpg dataset. We've seen that the average miles per gallon for cars has increased over time, but how has the average horsepower for cars changed over time? And does this trend differ by country of origin?
Instructions 1/3
Use relplot() and the mpg DataFrame to create a line plot with "model_year" on the x-axis and "horsepower" on the y-axis. Turn off the confidence intervals on the plot.
Instructions 2/3
Create different lines for each country of origin ("origin") that vary in both line style and color.
Instructions 3/3
Add markers for each data point to the lines.
Use the dashes parameter to use solid lines for all countries, while still allowing for different marker styles for each line.
"""
# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create line plot of model year vs. horsepower
sns.relplot(
    kind="line",
    data=mpg,
    x="model_year",
    y="horsepower",
    ci=None,
)

# Show plot
plt.show()



# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Change to create subgroups for country of origin
sns.relplot(x="model_year", y="horsepower", 
            data=mpg, kind="line", 
            style="origin",
            hue="origin",
            ci=None)

# Show plot
plt.show()



# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Add markers and make each line have the same style
sns.relplot(x="model_year", y="horsepower", 
            data=mpg, kind="line", 
            ci=None, style="origin", 
            hue="origin",
            markers=True,
            dashes=False)

# Show plot
plt.show()
