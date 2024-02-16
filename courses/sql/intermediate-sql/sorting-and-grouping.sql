/* Sorting single fields
Now that you understand how ORDER BY works, you'll put it into practice. In this exercise, you'll work on sorting single fields only. This can be helpful to extract quick insights such as the top-grossing or top-scoring film.

The following exercises will help you gain further insights into the film database.

Instructions 1/2
Select the name of each person in the people table, sorted alphabetically.
Instructions 2/2
Select the title and duration for every film, from longest duration to shortest.
*/

-- Select name from people and sort alphabetically
SELECT name 
FROM people 
ORDER BY name;

-- Select the title and duration from longest to shortest film
SELECT title, duration 
FROM films 
ORDER BY duration DESC;



/* Sorting multiple fields
ORDER BY can also be used to sort on multiple fields. It will sort by the first field specified, then sort by the next, and so on. As an example, you may want to sort the people data by age and keep the names in alphabetical order.

Try using ORDER BY to sort multiple columns.

Instructions 1/2
Select the release_year, duration, and title of films ordered by their release year and duration, in that order.
Instructions 2/2
Select the certification, release_year, and title from films ordered first by certification (alphabetically) and second by release year, starting with the most recent year.
*/

-- Select the release year, duration, and title sorted by release year and duration
SELECT release_year, duration, title 
FROM films 
ORDER BY release_year, duration;

-- Select the certification, release year, and title sorted by certification and release year
SELECT certification, release_year, title 
FROM films 
ORDER BY certification, release_year;




/* GROUP BY single fields
GROUP BY is a SQL keyword that allows you to group and summarize results with the additional use of aggregate functions. For example, films can be grouped by the certification and language before counting the film titles in each group. This allows you to see how many films had a particular certification and language grouping.

In the following steps, you'll summarize other groups of films to learn more about the films in your database.

Instructions 1/2
Select the release_year and count of films released in each year aliased as film_count.
Instructions 2/2
Select the release_year and average duration aliased as avg_duration of all films, grouped by release_year.
*/

-- Find the release_year and film_count of each year
SELECT release_year, COUNT(*) AS film_count 
FROM films 
GROUP BY release_year;


-- Find the release_year and average duration of films for each year
SELECT release_year, AVG(duration) AS avg_duration 
FROM films 
GROUP BY release_year;





/* GROUP BY multiple fields
GROUP BY becomes more powerful when used across multiple fields or combined with ORDER BY and LIMIT.

Perhaps you're interested in learning about budget changes throughout the years in individual countries. You'll use grouping in this exercise to look at the maximum budget for each country in each year there is data available.

Instructions
Select the release_year, country, and the maximum budget aliased as max_budget for each year and each country; sort your results by release_year and country.
*/

-- Find the release_year, country, and max_budget, then group and order by release_year and country
SELECT release_year, country, MAX(budget) AS max_budget 
FROM films 
GROUP BY release_year, country 
ORDER by release_year, country;




/* Filter with HAVING
Your final keyword is HAVING. It works similarly to WHERE in that it is a filtering clause, with the difference that HAVING filters grouped data.

Filtering grouped data can be especially handy when working with a large dataset. When working with thousands or even millions of rows, HAVING will allow you to filter for just the group of data you want, such as films over two hours in length!

Practice using HAVING to find out which countries (or country) have the most varied film certifications.

Instructions
Select country from the films table, and get the distinct count of certification aliased as certification_count.
Group the results by country.
Filter the unique count of certifications to only results greater than 10.
*/

-- Select the country and distinct count of certification as certification_count
SELECT 
    country, 
    COUNT(DISTINCT certification) AS certification_count
FROM films 
-- Group by country
GROUP BY country
-- Filter results to countries with more than 10 different certifications
HAVING COUNT(DISTINCT certification) > 10;



/* HAVING and sorting
Filtering and sorting go hand in hand and gives you greater interpretability by ordering our results.

Let's see this magic at work by writing a query showing what countries have the highest average film budgets.

Instructions
Select the country and the average budget as average_budget, rounded to two decimal, from films.
Group the results by country.
Filter the results to countries with an average budget of more than one billion (1000000000).
Sort by descending order of the average_budget.
*/

-- Select the country and average_budget from films
SELECT country, AVG(budget) AS average_budget
FROM films
-- Group by country
GROUP BY country
-- Filter to countries with an average_budget of more than one billion
HAVING AVG(budget) > 1000000000
-- Order by descending order of the aggregated budget
ORDER BY average_budget DESC;




/* All together now
It's time to use much of what you've learned in one query! This is good preparation for using SQL in the real world where you'll often be asked to write more complex queries since some of the basic queries can be answered by playing around in spreadsheet applications.

In this exercise, you'll write a query that returns the average budget and gross earnings for films each year after 1990 if the average budget is greater than 60 million.

This will be a big query, but you can handle it!

Instructions 1/4
Select the release_year for each film in the films table, filter for records released after 1990, and group by release_year.
Instructions 2/4
Modify the query to include the average budget aliased as avg_budget and average gross aliased as avg_gross for the results we have so far.
Instructions 3/4
Modify the query once more so that only years with an average budget of greater than 60 million are included.
Instructions 4/4
Finally, order the results from the highest average gross and limit to one.
*/

-- Select the release_year for films released after 1990 grouped by year
SELECT release_year 
FROM films
GROUP BY release_year
HAVING release_year > 1990;


-- Modify the query to also list the average budget and average gross
SELECT release_year, AVG(budget) AS avg_budget, AVG(gross) AS avg_gross
FROM films
WHERE release_year > 1990
GROUP BY release_year;


SELECT release_year, AVG(budget) AS avg_budget, AVG(gross) AS avg_gross
FROM films
WHERE release_year > 1990
GROUP BY release_year
-- Modify the query to see only years with an avg_budget of more than 60 million
HAVING AVG(budget) > 60000000;


SELECT release_year, AVG(budget) AS avg_budget, AVG(gross) AS avg_gross
FROM films
WHERE release_year > 1990
GROUP BY release_year
HAVING AVG(budget) > 60000000
-- Order the results from highest to lowest average gross and limit to one
ORDER BY avg_gross DESC
LIMIT 1;