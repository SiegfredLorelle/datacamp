""" The database schema
By now, you know that SQL databases always have a database schema. In the video on databases, you saw the following diagram:

Database Schema for Customer and Order

A PostgreSQL database is set up in your local environment, which contains this database schema. It's been filled with some example data. You can use pandas to query the database using the read_sql() function. You'll have to pass it a database engine, which has been defined for you and is called db_engine.

The pandas package imported as pd will store the query result into a DataFrame object, so you can use any DataFrame functionality on it after fetching the results from the database.

Instructions
Complete the SELECT statement so it selects the first_name and the last_name in the "Customer" table. Make sure to order by the last name first and the first name second.
Use the .head() method to show the first 3 rows of data.
Use .info() to show some general information about data.
"""
import pandas as pd

# Complete the SELECT statement
data = pd.read_sql("""
SELECT first_name, last_name FROM "Customer"
ORDER BY last_name, first_name
""", db_engine)

# Show the first 3 rows of the DataFrame
print(data.head(3))

# Show the info of the DataFrame
print(data.info())



""" Joining on relations
You've used the following diagram in the previous exercise:

Database Schema for Customer and Order

You've learned that you can use the read_sql() function from pandas to query the database. The real power of SQL is the ability to join information from multiple tables quickly. You do this by using the JOIN statement.

When joining two or more tables, pandas puts all the columns of the query result into a DataFrame.

Instructions
100 XP
Complete the SELECT statement, so it joins the "Customer" with the "Order" table.
Print the id column of data. What do you see?

"""

# Complete the SELECT statement
data = pd.read_sql("""
SELECT * FROM "Customer"
INNER JOIN "Order"
ON "Order"."customer_id"="Customer"."id"
""", db_engine)

# Show the id column of data
print(data.id)



""" From task to subtasks
For this exercise, you will be using parallel computing to apply the function take_mean_age() that calculates the average athlete's age in a given year in the Olympics events dataset. The DataFrame athlete_events has been loaded for you and contains amongst others, two columns:

Year: the year the Olympic event took place
Age: the age of the Olympian
You will be using the multiprocessor.Pool API which allows you to distribute your workload over several processes. The function parallel_apply() is defined in the sample code. It takes in as input the function being applied, the grouping used, and the number of cores needed for the analysis. Note that the @print_timing decorator is used to time each operation.

Instructions
Complete the code, so you apply take_mean_age with 1 core first, then 2 and finally 4 cores.
"""

# Function to apply a function over multiple cores
@print_timing
def parallel_apply(apply_func, groups, nb_cores):
    with Pool(nb_cores) as p:
        results = p.map(apply_func, groups)
    return pd.concat(results)

# Parallel apply using 1 core
parallel_apply(take_mean_age, athlete_events.groupby('Year'), 1)

# Parallel apply using 2 cores
parallel_apply(take_mean_age, athlete_events.groupby('Year'), 2)

# Parallel apply using 4 cores
parallel_apply(take_mean_age, athlete_events.groupby('Year'), 4)




""" Using a DataFrame
In the previous exercise, you saw how to split up a task and use the low-level python multiprocessing.Pool API to do calculations on several processing units.

It's essential to understand this on a lower level, but in reality, you'll never use this kind of APIs. A more convenient way to parallelize an apply over several groups is using the dask framework and its abstraction of the pandas DataFrame, for example.

The pandas DataFrame, athlete_events, is available in your workspace.

Instructions 1/2
Create 4 partitions of the athletes_events DataFrame using dd.from_pandas().
If you forgot the parameters of dd.from_pandas(), check out the slides again, or type help(dd.from_pandas) in the console!

Instructions 2/2
Print out the mean age for each Year. Remember dask uses lazy evaluation.
"""

import dask.dataframe as dd

# Set the number of partitions
athlete_events_dask = dd.from_pandas(athlete_events, npartitions=4)

# Calculate the mean Age per Year
print(athlete_events_dask.groupby('Year').Age.mean().compute())




""" A PySpark groupby
You've seen how to use the dask framework and its DataFrame abstraction to do some calculations. However, as you've seen in the video, in the big data world Spark is probably a more popular choice for data processing.

In this exercise, you'll use the PySpark package to handle a Spark DataFrame. The data is the same as in previous exercises: participants of Olympic events between 1896 and 2016.

The Spark Dataframe, athlete_events_spark is available in your workspace.

The methods you're going to use in this exercise are:

.printSchema(): helps print the schema of a Spark DataFrame.
.groupBy(): grouping statement for an aggregation.
.mean(): take the mean over each group.
.show(): show the results.

Instructions
Find out the type of athlete_events_spark.
Find out the schema of athlete_events_spark.
Print out the mean age of the Olympians, grouped by year. Notice that spark has not actually calculated anything yet. You can call this lazy evaluation.
Take the previous result, and call .show() on the result to calculate the mean age.
"""

# Print the type of athlete_events_spark
print(type(athlete_events_spark))

# Print the schema of athlete_events_spark
print(athlete_events_spark.printSchema())

# Group by the Year, and find the mean Age
print(athlete_events_spark.groupBy('Year').mean("Age"))

# Group by the Year, and find the mean Age
print(athlete_events_spark.groupBy('Year').mean("Age").show())




""" Airflow DAGs
In Airflow, a pipeline is represented as a Directed Acyclic Graph or DAG. The nodes of the graph represent tasks that are executed. The directed connections between nodes represent dependencies between the tasks.

Representing a data pipeline as a DAG makes much sense, as some tasks need to finish before others can start. You could compare this to an assembly line in a car factory. The tasks build up, and each task can depend on previous tasks being finished. A fictional DAG could look something like this:

Example DAG

Assembling the frame happens first, then the body and tires and finally you paint. Let's reproduce the example above in code.

Instructions 1/2
First, the DAG needs to run on every hour at minute 0. Fill in the schedule_interval keyword argument using the crontab notation. For example, every hour at minute N would be N * * * *. Remember, you need to run at minute 0.
Instructions 2/2
The downstream flow should match what you can see in the image above. The first step has already been filled in for you.
"""

# Create the DAG object
dag = DAG(dag_id="car_factory_simulation",
          default_args={"owner": "airflow","start_date": airflow.utils.dates.days_ago(2)},
          schedule_interval="0 * * * *")

# Task definitions
assemble_frame = BashOperator(task_id="assemble_frame", bash_command='echo "Assembling frame"', dag=dag)
place_tires = BashOperator(task_id="place_tires", bash_command='echo "Placing tires"', dag=dag)
assemble_body = BashOperator(task_id="assemble_body", bash_command='echo "Assembling body"', dag=dag)
apply_paint = BashOperator(task_id="apply_paint", bash_command='echo "Applying paint"', dag=dag)

# Complete the downstream flow
assemble_frame.set_downstream(place_tires)
assemble_frame.set_downstream(assemble_body)
assemble_body.set_downstream(apply_paint)