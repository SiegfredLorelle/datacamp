/* Practice with COUNT()
As you've seen, COUNT(*) tells you how many records are in a table. However, if you want to count the number of non-missing values in a particular field, you can call COUNT() on just that field.

Let's get some practice with COUNT()! You can look at the data in the tables throughout these exercises by clicking on the table name in the console.

Instructions 1/3
Count the total number of records in the people table, aliasing the result as count_records.
Instructions 2/3
Count the number of records with a birthdate in the people table, aliasing the result as count_birthdate.
Instructions 3/3
Count the records for languages and countries in the films table; alias as count_languages and count_countries.
*/

-- Count the number of records in the people table
SELECT COUNT(*) AS count_records 
FROM people;

-- Count the number of birthdates in the people table
SELECT COUNT(birthdate) AS count_birthdate 
FROM people;

-- Count the records for languages and countries represented in the films table
SELECT COUNT(language) AS count_languages, COUNT(country) AS count_countries 
FROM films;



/* SELECT DISTINCT
Often query results will include many duplicate values. You can use the DISTINCT keyword to select the unique values from a field.

This might be useful if, for example, you're interested in knowing which languages are represented in the films table. See if you can find out what countries are represented in this table with the following exercises.

Instructions 1/2
Return the unique countries represented in the films table using DISTINCT.
Instructions 2/2
Return the number of unique countries represented in the films table, aliased as count_distinct_countries.
*/

-- Return the unique countries from the films table
SELECT DISTINCT country 
FROM films;

-- Count the distinct countries from the films table
SELECT COUNT(DISTINCT country) AS count_distinct_countries  
FROM films;




/* Debugging errors
Debugging is an essential skill for all coders, and it comes from making many mistakes and learning from them.

In this exercise, you'll be given some buggy code that you'll need to fix.

Instructions 1/3
Debug and fix the SQL query provided.
Instructions 2/3
Find the two errors in this code; the same error has been repeated twice.
Instructions 3/3
Find the two bugs in this final query.
*/

-- Debug this code
SELECT certification
FROM films
LIMIT 5;

-- Debug this code
SELECT film_id, imdb_score, num_votes
FROM reviews;

-- Debug this code
SELECT COUNT(birthdate) AS count_birthdays
FROM people;




/* Formatting
Readable code is highly valued in the coding community and professional settings. Without proper formatting, code and results can be difficult to interpret. You'll often be working with other people that need to understand your code or be able to explain your results, so having a solid formatting habit is essential.

In this exercise, you'll correct poorly written code to better adhere to SQL style standards.

Instructions
Adjust the sample code so that it is in line with standard practices.
*/

-- Rewrite this query
SELECT person_id, role 
FROM roles 
LIMIT 10;

