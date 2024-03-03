/* Semi join
Great job getting acquainted with semi joins and anti joins! You are now going to practice using semi joins.

Let's say you are interested in identifying languages spoken in the Middle East. The languages table contains information about languages and countries, but it does not tell you what region the countries belong to. You can build up a semi join by filtering the countries table by a particular region, and then using this to further filter the languages table.

You'll build up your semi join as you did in the video exercise, block by block, starting with a selection of countries from the countries table, and then leveraging a WHERE clause to filter the languages table by this selection.

Instructions 1/3
Select country code as a single field from the countries table, filtering for countries in the 'Middle East' region.
Instructions 2/3
Write a second query to SELECT the name of each unique language appearing in the languages table; do not use column aliases here.
Order the result set by name in ascending order.
Instructions 3/3
Create a semi join out of the two queries you've written, which filters unique languages returned in the first query for only those languages spoken in the 'Middle East'.
*/

-- Select country code for countries in the Middle East
SELECT code 
FROM countries
WHERE region = 'Middle East';

-- Select unique language names
SELECT DISTINCT name
FROM languages
-- Order by the name of the language
ORDER BY name;

SELECT DISTINCT name
FROM languages
-- Add syntax to use bracketed subquery below as a filter
WHERE code IN
    (SELECT code
    FROM countries
    WHERE region = 'Middle East')
ORDER BY name;




/* Diagnosing problems using anti join
Nice work on semi joins! The anti join is a related and powerful joining tool. It can be particularly useful for identifying whether an incorrect number of records appears in a join.

Say you are interested in identifying currencies of Oceanian countries. You have written the following INNER JOIN, which returns 15 records. Now, you want to ensure that all Oceanian countries from the countries table are included in this result. You'll do this in the first step.

SELECT c1.code, name, basic_unit AS currency
FROM countries AS c1
INNER JOIN currencies AS c2
ON c1.code = c2.code
WHERE c1.continent = 'Oceania';
If there are any Oceanian countries excluded in this INNER JOIN, you want to return the names of these countries. You'll write an anti join to this in the second step!

Instructions 1/2
Begin by writing a query to return the code and name (in order, not aliased) for all countries in the continent of Oceania from the countries table.
Observe the number of records returned and compare this with the provided INNER JOIN, which returns 15 records.
Instructions 2/2
Now, build on your query to complete your anti join, by adding an additional filter to return every country code that is not included in the currencies table.
*/

-- Select code and name of countries from Oceania
SELECT 
    code,
    name
FROM countries
WHERE continent = 'Oceania';


SELECT code, name
FROM countries
WHERE continent = 'Oceania'
-- Filter for countries not included in the bracketed subquery
  AND code NOT IN
    (SELECT code
    FROM currencies);




/* Subquery inside WHERE
The video pointed out that subqueries inside WHERE can either be from the same table or a different table. In this exercise, you will nest a subquery from the populations table inside another query from the same table, populations. Your goal is to figure out which countries had high average life expectancies in 2015.

You can use SQL to do calculations for you. Suppose you only want records from 2015 with life_expectancy above 1.15 * avg_life_expectancy. You could use the following SQL query.

SELECT *
FROM populations
WHERE life_expectancy > 1.15 * avg_life_expectancy
  AND year = 2015;
In the first step, you'll write a query to calculate a value for avg_life_expectancy. In the second step, you will nest this calculation into another query.

Instructions 1/2
Begin by calculating the average life expectancy from the populations table.
Filter your answer to use records from 2015 only.
Instructions 2/2
The answer from your query has now been nested into another query; use this calculation to filter populations for all records where life_expectancy is 1.15 times higher than average.
*/

-- Select average life_expectancy from the populations table
SELECT AVG(life_expectancy)
-- Filter for the year 2015
FROM populations 
WHERE year = 2015;

SELECT *
FROM populations
-- Filter for only those populations where life expectancy is 1.15 times higher than average
WHERE life_expectancy > 1.15 *
  (SELECT AVG(life_expectancy)
   FROM populations
   WHERE year = 2015) 
    AND year = 2015;




/* WHERE do people live?
In this exercise, you will strengthen your knowledge of subquerying by identifying capital cities in order of largest to smallest population.

Follow the instructions below to get the urban area population for capital cities only. You'll use the countries and cities tables displayed in the console to help identify columns of interest as you build your query.

Instructions
Return the name, country_code and urbanarea_pop for all capital cities (not aliased).
*/

-- Select relevant fields from cities table
SELECT name, country_code, urbanarea_pop
FROM cities 
-- Filter using a subquery on the countries table
WHERE name IN (
SELECT capital FROM countries
)
ORDER BY urbanarea_pop DESC;





/* Subquery inside SELECT
As explored in the video, there are often multiple ways to produce the same result in SQL. You saw that subqueries can provide an alternative to joins to obtain the same result.

In this exercise, you'll go further in exploring how some queries can be written using either a join or a subquery.

In Step 1, you'll begin with a LEFT JOIN combined with a GROUP BY to select the nine countries with the most cities appearing in the cities table, along with the counts of these cities. In Step 2, you'll write a query that returns the same result as the join, but leveraging a nested query instead.

Instructions 1/2
Write a LEFT JOIN with countries on the left and the cities on the right, joining on country code.
In the SELECT statement of your join, include country names as country, and count the cities in each country, aliased as cities_num.
Sort by cities_num (descending), and country (ascending), limiting to the first nine records.
Instructions 2/2
Complete the subquery to return a result equivalent to your LEFT JOIN, counting all cities in the cities table as cities_num.
Use the WHERE clause to enable the correct country codes to be matched in the cities and countries columns.
*/

-- Find top nine countries with the most cities
SELECT 
    countries.name AS country,
    COUNT(countries.name) AS cities_num
FROM countries
LEFT JOIN cities
ON countries.code = cities.country_code
GROUP BY countries.name
-- Order by count of cities as cities_num
ORDER BY 
    cities_num DESC,
    country ASC
LIMIT 9;


SELECT countries.name AS country,
-- Subquery that provides the count of cities   
  (SELECT COUNT(*)
   FROM cities
   WHERE cities.country_code = code) AS cities_num
FROM countries
ORDER BY cities_num DESC, country
LIMIT 9;




/* Subquery inside FROM
Subqueries inside FROM can help select columns from multiple tables in a single query.

Say you are interested in determining the number of languages spoken for each country. You want to present this information alongside each country's local_name, which is a field only present in the countries table and not in the languages table. You'll use a subquery inside FROM to bring information from these two tables together!

Instructions 1/2
Begin with a query that groups by each country code from languages, and counts the languages spoken in each country as lang_num.
In your SELECT statement, return code and lang_num (in that order).
Instructions 2/2
Select local_name from countries, with the aliased lang_num from your subquery (which has been nested and aliased for you as sub).
Use WHERE to match the code field from countries and sub.
*/

-- Select code, and language count as lang_num
SELECT 
    code, 
    COUNT(name) AS lang_num
FROM languages 
GROUP BY code;

-- Select code, and language count as lang_num
SELECT 
    code, 
    COUNT(name) AS lang_num
FROM languages 
GROUP BY code;



/* Subquery challenge
You're near the finish line! Test your understanding of subquerying with a challenge problem.

Suppose you're interested in analyzing inflation and unemployment rate for certain countries in 2015. You are not interested in countries with "Republic" or "Monarchy" as their form of government, but are interested in all other forms of government, such as emirate federations, socialist states, and commonwealths.

You will use the field gov_form to filter for these two conditions, which represents a country's form of government. You can review the different entries for gov_form in the countries table.

Instructions
Select country code, inflation_rate, and unemployment_rate from economies.
Filter code for the set of countries which do not contain the words "Republic" or "Monarchy" in their gov_form.
*/

-- Select relevant fields
SELECT 
  code, 
  inflation_rate, 
  unemployment_rate
FROM economies
WHERE year = 2015 
  AND code NOT IN
-- Subquery returning country codes filtered on gov_form
	(SELECT code
  FROM countries
  WHERE 
    gov_form LIKE '%Monarchy%'
    OR gov_form LIKE '%Republic%')
ORDER BY inflation_rate;




/* Final challenge
You've made it to the final challenge problem! Get ready to tackle this step-by-step.

Your task is to determine the top 10 capital cities in Europe and the Americas by city_perc, a metric you'll calculate. city_perc is a percentage that calculates the "proper" population in a city as a percentage of the total population in the wider metro area, as follows:

city_proper_pop / metroarea_pop * 100

Do not use table aliasing in this exercise.

Instructions
From cities, select the city name, country code, proper population, and metro area population, as well as the field city_perc, which calculates the proper population as a percentage of metro area population for each city (using the formula provided).
Filter city name with a subquery that selects capital cities from countries in 'Europe' or continents with 'America' at the end of their name.
Exclude NULL values in metroarea_pop.
Order by city_perc (descending) and return only the first 10 rows.
*/

-- Select fields from cities
SELECT 
    name,
    country_code, 
    city_proper_pop, 
    metroarea_pop, 
    (city_proper_pop / metroarea_pop) * 100 AS city_perc
FROM cities
-- Use subquery to filter city name
WHERE 
    name IN 
        (SELECT capital
        FROM countries
        WHERE continent = 'Europe'
            OR continent LIKE '%America')
-- Add filter condition such that metroarea_pop does not have null values
    AND metroarea_pop IS NOT NULL
-- Sort and limit the result
ORDER BY city_perc DESC
LIMIT 10;