""" Querying the table
Now that you have a grasp of what's happening in the datacamp_application database, let's go ahead and write up a query for that database.

The goal is to get a feeling for the data in this exercise. You'll get the rating data for three sample users and then use a predefined helper function, print_user_comparison(), to compare the sets of course ids these users rated.

Instructions
Complete the connection URI. The database is called datacamp_application. The host is localhost with port 5432. The username is repl and the password is password.
Select the ratings of users with id: 4387, 18163 and 8770.
Fill in print_user_comparison() with the three users you selected.
"""
import sqlalchemy
import pandas as pd

# Complete the connection URI
connection_uri = "postgresql://repl:password@localhost:5432/datacamp_application" 
db_engine = sqlalchemy.create_engine(connection_uri)

# Get user with id 4387
user1 = pd.read_sql("SELECT * FROM rating WHERE user_id='4387'", db_engine)

# Get user with id 18163
user2 = pd.read_sql("SELECT * FROM rating WHERE user_id='18163'", db_engine)

# Get user with id 8770
user3 = pd.read_sql("SELECT * FROM rating WHERE user_id='8770'", db_engine)

# Use the helper function to compare the 3 users
print_user_comparison(user1, user2, user3)




""" Average rating per course
A great way to recommend courses is to recommend top-rated courses, as DataCamp students often like courses that are highly rated by their peers.

In this exercise, you'll complete a transformation function transform_avg_rating() that aggregates the rating data using the pandas DataFrame's .groupby() method. The goal is to get a DataFrame with two columns, a course id and its average rating:

course_id	avg_rating
123	4.72
111	4.62
…	…
In this exercise, you'll complete this transformation function, and apply it on raw rating data extracted via the helper function extract_rating_data() which extracts course ratings from the rating table.

Instructions
Complete the transform_avg_rating() function by grouping by the course_id column, and taking the mean of the rating column.
Use extract_rating_data() to extract raw ratings data. It takes in as argument the database engine db_engines.
Use transform_avg_rating() on the raw rating data you've extracted.

"""

# Complete the transformation function
def transform_avg_rating(rating_data):
    # Group by course_id and extract average rating per course
    avg_rating = rating_data.groupby('course_id').rating.mean()
    # Return sorted average ratings per course
    sort_rating = avg_rating.sort_values(ascending=False).reset_index()
    return sort_rating

# Extract the rating data into a DataFrame
rating_data = extract_rating_data(db_engines)

# Use transform_avg_rating on the extracted data and print results
avg_rating_data = transform_avg_rating(rating_data)
print(avg_rating_data) 



""" Filter out corrupt data
One recurrent step you can expect in the transformation phase would be to clean up some incomplete data. In this exercise, you're going to look at course data, which has the following format:

course_id	title	description	programming_language
1	Some Course	…	r
You're going to inspect this DataFrame and make sure there are no missing values by using the pandas DataFrame's .isnull().sum() methods. You will find that the programming_language column has some missing values.

As such, you will complete the transform_fill_programming_language() function by using the .fillna() method to fill missing values.

Instructions
Print the number of missing values in course_data.
Missing values of the programming_language should be the language "R".
Print out the number of missing values per column once more, this time for transformed.
"""

course_data = extract_course_data(db_engines)

# Print out the number of missing values per column
print(course_data.isnull().sum())

# The transformation should fill in the missing values
def transform_fill_programming_language(course_data):
    imputed = course_data.fillna({"programming_language": "R"})
    return imputed

transformed = transform_fill_programming_language(course_data)

# Print out the number of missing values per column of transformed
print(transformed.isnull().sum())



""" Using the recommender transformation
In the last few exercises, you calculated the average rating per course and cleaned up some course data. You will use this data to produce viable recommendations for DataCamp students.

As a reminder, here are the decision rules for producing recommendations:

Use technology a student has rated the most.
Exclude courses a student has already rated.
Find the three top-rated courses from eligible courses.
In order to produce the final recommendations, you will use the average course ratings, and the list of eligible recommendations per user, stored in avg_course_ratings and courses_to_recommend respectively. You will do this by completing the transform_recommendations() function which merges both DataFrames and finds the top 3 highest rated courses to recommend per user.

Instructions
Complete the transform_recommendations() function:
Merge course_to_recommend with avg_course_ratings.
Sort the results by rating, grouping by user ID.
Show the top 3 rows and sort by user ID.
Call the transform_recommendations() function you just defined with the appropriate arguments to store recommendations per user in the recommendations variable.
"""

# Complete the transformation function
def transform_recommendations(avg_course_ratings, courses_to_recommend):
    # Merge both DataFrames
    merged = courses_to_recommend.merge(avg_course_ratings) 
    # Sort values by rating and group by user_id
    grouped = merged.sort_values("rating", ascending=False).groupby("user_id")
    # Produce the top 3 values and sort by user_id
    recommendations = grouped.head(3).sort_values("user_id").reset_index()
    final_recommendations = recommendations[["user_id", "course_id","rating"]]
    # Return final recommendations
    return final_recommendations

# Use the function with the predefined DataFrame objects
recommendations = transform_recommendations(avg_course_ratings, courses_to_recommend)



""" The target table
In the previous exercises, you've calculated a DataFrame called recommendations. It contains pairs of user_id's' and course_id's, with a rating that represents the average rating of this course. The assumption is the highest rated course, which is eligible for a user would be best to recommend.

It's time to put this table into a database so that it can be used by several products like a recommendation engine or an emailing system.

Since it's a pandas.DataFrame object, you can use the .to_sql() method. Of course, you'll have to connect to the database using the connection URI first. The recommendations table is available in your environment.

Instructions
Fill in the connection URI for the Postgres database on host localhost with port 5432. You can connect with user repl and password password. The database name is dwh.
Complete the load_to_dwh() function. It should write to the "recommendations" table and replace the table if it already exists.
"""

connection_uri = "postgresql://repl:password@localhost:5432/dwh"
db_engine = sqlalchemy.create_engine(connection_uri)

def load_to_dwh(recommendations):
    recommendations.to_sql("recommendations", db_engine, if_exists="replace")




""" Defining the DAG
In the previous exercises, you've completed the extract, transform and load phases separately. Now all of this is put together in one neat etl() function that you can discover in the console.

The etl() function extracts raw course and ratings data from relevant databases, cleans corrupt data and fills in missing value, computes average rating per course and creates recommendations based on the decision rules for producing recommendations, and finally loads the recommendations into a database.

As you might remember from the video, etl() accepts a single argument: db_engines. You can pass this to the task using op_kwargs in the PythonOperator. You can pass it a dictionary that will be filled in as kwargs in the callable.

Instructions
Complete the DAG definition, so it runs daily. Make sure to use the cron notation.
Complete the PythonOperator() by passing the correct arguments. Other than etl, db_engines is also available in your workspace.
"""

# Define the DAG so it runs on a daily basis
dag = DAG(dag_id="recommendations",
          schedule_interval="0 0 * * *")

# Make sure `etl()` is called in the operator. Pass the correct kwargs.
task_recommendations = PythonOperator(
    task_id="recommendations_task",
    python_callable=etl,
    op_kwargs={"db_engines": db_engines},
)




""" Querying the recommendations
In the previous exercises, you've learned how to calculate a table with course recommendations on a daily basis. Now that this recommendations table is in the data warehouse, you could also quickly join it with other tables in order to produce important features for DataCamp students such as customized marketing emails, intelligent recommendations for students and other features.

In this exercise, you will get a taste of how the newly created recommendations table could be utilized by creating a function recommendations_for_user() which automatically gets the top recommended courses based per user ID for a particular rating threshold.

Instructions
Complete the query in the recommendations_for_user() function definition. It should join the courses table.
Complete the read_sql() function in recommendations_for_user(). The params argument is incomplete: it's missing a threshold.
Run the recommendations_for_user() function you defined in the last statements and observe the results.
"""

def recommendations_for_user(user_id, threshold=4.5):
    # Join with the courses table
    query = """
    SELECT title, rating FROM recommendations
    INNER JOIN courses ON courses.course_id = recommendations.course_id
    WHERE user_id=%(user_id)s AND rating>%(threshold)s
    ORDER BY rating DESC
    """
    # Add the threshold parameter
    predictions_df = pd.read_sql(query, db_engine, params = {"user_id": user_id, 
                                                             "threshold": threshold})
    return predictions_df.title.values

# Try the function you created
print(recommendations_for_user(12, 4.65))