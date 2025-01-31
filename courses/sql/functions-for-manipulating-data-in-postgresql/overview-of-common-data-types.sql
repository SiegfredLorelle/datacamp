/* Getting information about your database
As we saw in the video, PostgreSQL has a system database called INFORMATION_SCHEMA that allows us to extract information about objects, including tables, in our database.

In this exercise we will look at how to query the tables table of the INFORMATION_SCHEMA database to discover information about tables in the DVD Rentals database including the name, type, schema, and catalog of all tables and views and then how to use the results to get additional information about columns in our tables.

Instructions 1/2
Select all columns from the INFORMATION_SCHEMA.TABLES system database. Limit results that have a public table_schema.
Instructions 2/2
Select all columns from the INFORMATION_SCHEMA.COLUMNS system database. Limit by table_name to actor
*/

-- Select all columns from the TABLES system database
SELECT * 
FROM INFORMATION_SCHEMA.TABLES
-- Filter by schema
WHERE table_schema = 'public';


-- Select all columns from the COLUMNS system database
SELECT * 
FROM INFORMATION_SCHEMA.COLUMNS
WHERE table_name = 'actor';




/* Determining data types
The columns table of the INFORMATION_SCHEMA database also allows us to extract information about the data types of columns in a table. We can extract information like the character or string length of a CHAR or VARCHAR column or the precision of a DECIMAL or NUMERIC floating point type.

Using the techniques you learned in the lesson, let's explore the customer table of our DVD Rental database.

Instructions
Select the column name and data type from the INFORMATION_SCHEMA.COLUMNS system database.
Limit results to only include the customer table.
*/

-- Get the column name and data type
SELECT
  column_name, 
  data_type
-- From the system database information schema
FROM INFORMATION_SCHEMA.COLUMNS 
-- For the customer table
WHERE table_name = 'customer';




/* Interval data types
INTERVAL data types provide you with a very useful tool for performing arithmetic on date and time data types. For example, let's say our rental policy requires a DVD to be returned within 3 days. We can calculate the expected_return_date for a given DVD rental by adding an INTERVAL of 3 days to the rental_date from the rental table. We can then compare this result to the actual return_date to determine if the DVD was returned late.

Let's try this example in the exercise.

Instructions
Select the rental date and return date from the rental table.
Add an INTERVAL of 3 days to the rental_date to calculate the expected return date`.
*/

SELECT
  -- Select the rental and return dates
	rental_date,
	return_date,
  -- Calculate the expected_return_date
	rental_date + INTERVAL '3 days' AS expected_return_date
FROM rental;




/* Accessing data in an ARRAY
In our DVD Rentals database, the film table contains an ARRAY for special_features which has a type of TEXT[]. Much like any ARRAY data type in PostgreSQL, a TEXT[] array can store an array of TEXT values. This comes in handy when you want to store things like phone numbers or email addresses as we saw in the lesson.

Let's take a look at the special_features column and also practice accessing data in the ARRAY.

Instructions 1/3
Select the title and special features from the film table and compare the results between the two columns.
Instructions 2/3
Select all films that have a special feature Trailers by filtering on the first index of the special_features ARRAY.
Instructions 3/3
Now let's select all films that have Deleted Scenes in the second index of the special_features ARRAY.
*/

-- Select the title and special features column 
SELECT 
  title, 
  special_features
FROM film;

-- Select the title and special features column 
SELECT 
  title, 
  special_features 
FROM film
-- Use the array index of the special_features column
WHERE special_features[1] = 'Trailers';

-- Select the title and special features column 
SELECT 
  title, 
  special_features 
FROM film
-- Use the array index of the special_features column
WHERE special_features[2] = 'Deleted Scenes';




/* Searching an ARRAY with ANY
As we saw in the video, PostgreSQL also provides the ability to filter results by searching for values in an ARRAY. The ANY function allows you to search for a value in any index position of an ARRAY. Here's an example.

WHERE 'search text' = ANY(array_name)
When using the ANY function, the value you are filtering on appears on the left side of the equation with the name of the ARRAY column as the parameter in the ANY function.

Instructions
Match 'Trailers' in any index of the special_features ARRAY regardless of position.
*/

SELECT
  title, 
  special_features 
FROM film 
-- Modify the query to use the ANY function 
WHERE 'Trailers' = ANY (special_features);



/* Searching an ARRAY with @>
The contains operator @> operator is alternative syntax to the ANY function and matches data in an ARRAY using the following syntax.

WHERE array_name @> ARRAY['search text'] :: type[]
So let's practice using this operator in the exercise.

Instructions
Use the contains operator to match the text Deleted Scenes in the special_features column.
*/

SELECT 
  title, 
  special_features 
FROM film 
-- Filter where special_features contains 'Deleted Scenes'
WHERE special_features @> ARRAY['Deleted Scenes'];