/* Deciding fact and dimension tables
Imagine that you love running and data. It's only natural that you begin collecting data on your weekly running routine. You're most concerned with tracking how long you are running each week. You also record the route and the distances of your runs. You gather this data and put it into one table called Runs with the following schema:

runs
duration_mins - float
week - int
month - varchar(160)
year - int
park_name - varchar(160)
city_name - varchar(160)
distance_km - float
route_name - varchar(160)
After learning about dimensional modeling, you decide to restructure the schema for the database. Runs has been pre-loaded for you.

Create a dimension table called route that will hold the route information.
Create a dimension table called week that will hold the week information.
*/

-- Create a route dimension table
CREATE TABLE route(
	route_id INTEGER PRIMARY KEY,
  park_name VARCHAR(160) NOT NULL,
  city_name VARCHAR(160) NOT NULL,
  distance_km FLOAT NOT NULL,
  route_name VARCHAR(160) NOT NULL
);
-- Create a week dimension table
CREATE TABLE week(
	week_id INTEGER PRIMARY KEY,
  week INTEGER NOT NULL,
  month VARCHAR(160) NOT NULL,
  year INTEGER NOT NULL
);




/* Querying the dimensional model
Here it is! The schema reorganized using the dimensional model: 

Let's try to run a query based on this schema. How about we try to find the number of minutes we ran in July, 2019? We'll break this up in two steps. First, we'll get the total number of minutes recorded in the database. Second, we'll narrow down that query to week_id's from July, 2019.

Instructions 1/2
Calculate the sum of the duration_mins column.
Instructions 2/2
Join week_dim and runs_fact.
Get all the week_id's from July, 2019.
*/

SELECT 
	-- Get the total duration of all runs
	SUM(duration_mins)
FROM 
	runs_fact
-- Get all the week_id's that are from July, 2019
INNER JOIN week_dim ON runs_fact.week_id = week_dim.week_id
WHERE month = 'July' and year = '2019';