/* Comparing global economies
Are you ready to perform your first set operation?

In this exercise, you have two tables, economies2015 and economies2019, available to you under the tabs in the console. You'll perform a set operation to stack all records in these two tables on top of each other, excluding duplicates.

When drafting queries containing set operations, it is often helpful to write the queries on either side of the operation first, and then call the set operator. The instructions are ordered accordingly.

Instructions
Begin your query by selecting all fields from economies2015.
Create a second query that selects all fields from economies2019.
Perform a set operation to combine the two queries you just created, ensuring you do not return duplicates.
*/

-- Select all fields from economies2015
SELECT *
FROM economies2015
-- Set operation
UNION
-- Select all fields from economies2019
SELECT *
FROM economies2019
ORDER BY code, year;




/* Comparing two set operations
You learned in the video exercise that UNION ALL returns duplicates, whereas UNION does not. In this exercise, you will dive deeper into this, looking at cases for when UNION is appropriate compared to UNION ALL.

You will be looking at combinations of country code and year from the economies and populations tables.

Instructions 1/2
Perform an appropriate set operation that determines all pairs of country code and year (in that order) from economies and populations, excluding duplicates.
Order by country code and year.
Instructions 2/2
Amend the query to return all combinations (including duplicates) of country code and year in the economies or the populations tables.
*/

-- Query that determines all pairs of code and year from economies and populations, without duplicates
SELECT country_code AS code, year
FROM populations
UNION
SELECT code,year
FROM economies
ORDER BY code, year;


SELECT code, year
FROM economies
-- Set theory clause
UNION ALL
SELECT country_code, year
FROM populations
ORDER BY code, year;




/* INTERSECT
Well done getting through the material on INTERSECT!

Let's say you are interested in those countries that share names with cities. Use this task as an opportunity to show off your knowledge of set theory in SQL!

Instructions
Return all city names that are also country names.
*/

-- Return all cities with the same name as a country
SELECT name
FROM cities
INTERSECT
SELECT name
FROM countries;




/* You've got it, EXCEPT...
Just as you were able to leverage INTERSECT to find the names of cities with the same names as countries, you can also do the reverse, using EXCEPT.

In this exercise, you will find the names of cities that do not have the same names as their countries.

Instructions
Return all cities that do not have the same name as a country.
*/

-- Return all cities that do not have the same name as a country
SELECT name 
FROM cities
EXCEPT 
SELECT name 
FROM countries
ORDER BY name;