/* Your first join
Throughout this course, you'll be working with the countries database, which contains information about the most populous world cities in the world, along with country-level economic, population, and geographic data. The database also contains information on languages spoken in each country.

You can see the different tables in this database to get a sense of what they contain by clicking on the corresponding tabs. Click through them and familiarize yourself with the fields that seem to be shared across tables before you continue with the course.

In this exercise, you'll use the cities and countries tables to build your first inner join. You'll start off by selecting all columns in step 1, performing your join in step 2, and then refining your join to choose specific columns in step 3.

Instructions 1/3
Begin by selecting all columns from the cities table, using the SQL shortcut that selects all.
Instructions 2/3
Perform an inner join with the cities table on the left and the countries table on the right; do not alias tables here or in the next step.
Identify the relevant column names to join ON by inspecting the cities and countries tabs in the console.
Instructions 3/3
Complete the SELECT statement to keep only the name of the city, the name of the country, and the region the country is located in (in the order specified).
Alias the name of the city AS city and the name of the country AS country.

*/

-- Select all columns from cities
SELECT * 
FROM cities;


SELECT * 
FROM cities
-- Inner join to countries
INNER JOIN countries
-- Match on country codes
ON cities.country_code = countries.code;


-- Select name fields (with alias) and region 
SELECT 
    cities.name AS city,
    countries.name AS country,  
    countries.region
FROM cities
INNER JOIN countries
ON cities.country_code = countries.code;




/* Joining with aliased tables
Recall from the video that instead of writing full table names in queries, you can use table aliasing as a shortcut. The alias can be used in other parts of your query, such as the SELECT statement!

You also learned that when you SELECT fields, a field can be ambiguous. For example, imagine two tables, apples and oranges, both containing a column called color. You need to use the syntax apples.color or oranges.color in your SELECT statement to point SQL to the correct table. Without this, you would get the following error:

column reference "color" is ambiguous
In this exercise, you'll practice joining with aliased tables. You'll use data from both the countries and economies tables to examine the inflation rate in 2010 and 2015.

When writing joins, many SQL users prefer to write the SELECT statement after writing the join code, in case the SELECT statement requires using table aliases.

Instructions
Start with your inner join in line 5; join the tables countries AS c (left) with economies (right), aliasing economies AS e.
Next, use code as your joining field in line 7; do not use the USING command here.
Lastly, select the following columns in order in line 2: code from the countries table (aliased as country_code), name, year, and inflation_rate.
*/

-- Select fields with aliases
SELECT 
    c.code AS country_code,
    name,
    year,
    inflation_rate
FROM countries AS c
-- Join to economies (alias e)
INNER JOIN economies AS e
-- Match on code field using table aliases
ON c.code = e.code





/* USING in action
In the previous exercises, you performed your joins using the ON keyword. Recall that when both the field names being joined on are the same, you can take advantage of the USING clause.

You'll now explore the languages table from our database. Which languages are official languages, and which ones are unofficial?

You'll employ USING to simplify your query as you explore this question.

Instructions
Use the country code field to complete the INNER JOIN with USING; do not change any alias names.
*/

SELECT c.name AS country, l.name AS language, official
FROM countries AS c
INNER JOIN languages AS l
-- Match using the code column
USING(code)




/* Inspecting a relationship
You've just identified that the countries table has a many-to-many relationship with the languages table. That is, many languages can be spoken in a country, and a language can be spoken in many countries.

This exercise looks at each of these in turn. First, what is the best way to query all the different languages spoken in a country? And second, how is this different from the best way to query all the countries that speak each language?

Recall that when writing joins, many users prefer to write SQL code out of order by writing the join first (along with any table aliases), and writing the SELECT statement at the end.

Instructions 1/3
Start with the join statement in line 6; perform an inner join with the countries table as c on the left with the languages table as l on the right.
Make use of the USING keyword to join on code in line 8.
Lastly, in line 2, select the country name, aliased as country, and the language name, aliased as language.
Instructions 2/3
Rearrange the SELECT statement so that the language column appears on the left and the country column on the right.
Sort the results by language.

*/

-- Select country and language names, aliased
SELECT c.name AS country, l.name AS language 
-- From countries (aliased)
FROM countries AS c
-- Join to languages (aliased)
INNER JOIN languages AS l
-- Use code as the joining field with the USING keyword
USING(code);


-- Rearrange SELECT statement, keeping aliases
SELECT l.name AS language, c.name AS country
FROM countries AS c
INNER JOIN languages AS l
USING(code)
-- Order the results by language
ORDER BY language;





/* Joining multiple tables
You've seen that the ability to combine multiple joins using a single query is a powerful feature of SQL.

Suppose you are interested in the relationship between fertility and unemployment rates. Your task in this exercise is to join tables to return the country name, year, fertility rate, and unemployment rate in a single result from the countries, populations and economies tables.

Instructions 1/2
Perform an inner join of countries AS c (left) with populations AS p (right), on code.
Select name, year and fertility_rate.
Instructions 2/2
Chain another inner join to your query with the economies table AS e, using code.
Select name, and using table aliases, select year and unemployment_rate from economies.
*/

-- Select relevant fields
SELECT name, year, fertility_rate
FROM countries AS c
-- Inner join countries and populations, aliased, on code
INNER JOIN populations AS p
ON c.code = p.country_code;

-- Select fields
SELECT name, p.year, fertility_rate, e.year, e.unemployment_rate
FROM countries AS c
INNER JOIN populations AS p
ON c.code = p.country_code
-- Join to economies (as e)
INNER JOIN economies AS e
-- Match on country code
USING(code);




/* Checking multi-table joins
Have a look at the results for Albania from the previous query below. You can see that the 2015 fertility_rate has been paired with 2010 unemployment_rate, and vice versa.

name	year	fertility_rate	unemployment_rate
Albania	2015	1.663	17.1
Albania	2010	1.663	14
Albania	2015	1.793	17.1
Albania	2010	1.793	14
Instead of four records, the query should return two: one for each year. The last join was performed on c.code = e.code, without also joining on year. Your task in this exercise is to fix your query by explicitly stating that both the country code and year should match!

Instructions
Modify your query so that you are joining to economies on year as well as code.
*/

SELECT name, e.year, fertility_rate, unemployment_rate
FROM countries AS c
INNER JOIN populations AS p
ON c.code = p.country_code
INNER JOIN economies AS e
ON c.code = e.code
-- Add an additional joining condition such that you are also joining on year
	AND p.year = e.year;