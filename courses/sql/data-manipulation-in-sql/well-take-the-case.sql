/* Basic CASE statements
What is your favorite team?

The European Soccer Database contains data about 12,800 matches from 11 countries played between 2011-2015! Throughout this course, you will be shown filtered versions of the tables in this database in order to better explore their contents.

In this exercise, you will identify matches played between FC Schalke 04 and FC Bayern Munich. There are 2 teams identified in each match in the hometeam_id and awayteam_id columns, available to you in the filtered matches_germany table. ID can join to the team_api_id column in the teams_germany table, but you cannot perform a join on both at the same time.

However, you can perform this operation using a CASE statement once you've identified the team_api_id associated with each team!

Instructions 1/2
Select the team's long name and API id from the teams_germany table.
Filter the query for FC Schalke 04 and FC Bayern Munich using IN, giving you the team_api_IDs needed for the next step.

Instructions 2/2
Create a CASE statement that identifies whether a match in Germany included FC Bayern Munich, FC Schalke 04, or neither as the home team.
Group the query by the CASE statement alias, home_team.
*/

SELECT
	-- Select the team long name and team API id
	ts.team_long_name,
	ts.team_api_Id
FROM teams_germany AS ts
-- Only include FC Schalke 04 and FC Bayern Munich
WHERE team_long_name IN ('FC Schalke 04', 'FC Bayern Munich');


-- Identify the home team as Bayern Munich, Schalke 04, or neither
SELECT 
	CASE WHEN hometeam_id = 10189 THEN 'FC Schalke 04'
        WHEN hometeam_id = 9823 THEN 'FC Bayern Munich'
        ELSE 'Other' END AS home_team,
	COUNT(id) AS total_matches
FROM matches_germany
-- Group by the CASE statement alias
GROUP BY home_team;



/* CASE statements comparing column values
Barcelona is considered one of the strongest teams in Spain's soccer league.

In this exercise, you will be creating a list of matches in the 2011/2012 season where Barcelona was the home team. You will do this using a CASE statement that compares the values of two columns to create a new group -- wins, losses, and ties.

In 3 steps, you will build a query that identifies a match's winner, identifies the identity of the opponent, and finally filters for Barcelona as the home team. Completing a query in this order will allow you to watch your results take shape with each new piece of information.

The matches_spain table currently contains Barcelona's matches from the 2011/2012 season, and has two key columns, hometeam_id and awayteam_id, that can be joined with the teams_spain table. However, you can only join teams_spain to one column at a time.

Instructions 1/3
Select the date of the match and create a CASE statement to identify matches as home wins, home losses, or ties.
Instructions 2/3
Left join the teams_spain table team_api_id column to the matches_spain table awayteam_id. This allows us to retrieve the away team's identity.
Select team_long_name from teams_spain as opponent and complete the CASE statement from Step 1.
Instructions 3/3
Complete the same CASE statement as the previous steps.
Filter for matches where the home team is FC Barcelona (id = 8634).
*/

SELECT 
	-- Select the date of the match
	date,
	-- Identify home wins, losses, or ties
	CASE WHEN home_goal > away_goal THEN 'Home win!'
        WHEN home_goal < away_goal THEN 'Home loss :(' 
        ELSE 'Tie' END AS outcome
FROM matches_spain;


SELECT 
	m.date,
	--Select the team long name column and call it 'opponent'
	t.team_long_name AS opponent, 
	-- Complete the CASE statement with an alias
	CASE WHEN m.home_goal > m.away_goal THEN 'Home win!'
        WHEN m.home_goal < m.away_goal THEN 'Home loss :('
        ELSE 'Tie' END AS outcome
FROM matches_spain AS m
-- Left join teams_spain onto matches_spain
LEFT JOIN teams_spain AS t
ON m.awayteam_id = t.team_api_Id;


SELECT 
	m.date,
	t.team_long_name AS opponent,
    -- Complete the CASE statement with an alias
	CASE WHEN m.home_goal > m.away_goal THEN 'Barcelona win!'
        WHEN m.home_goal < m.away_goal THEN 'Barcelona loss :(' 
        ELSE 'Tie' END AS outcome 
FROM matches_spain AS m
LEFT JOIN teams_spain AS t 
ON m.awayteam_id = t.team_api_id
-- Filter for Barcelona as the home team
WHERE m.hometeam_id = 8634; 



/* CASE statements comparing two column values part 2
Similar to the previous exercise, you will construct a query to determine the outcome of Barcelona's matches where they played as the away team. You will learn how to combine these two queries in chapters 2 and 3.

Did their performance differ from the matches where they were the home team?

Instructions
Complete the CASE statement to identify Barcelona's away team games (id = 8634) as wins, losses, or ties.
Left join the teams_spain table team_api_id column on the matches_spain table hometeam_id column. This retrieves the identity of the home team opponent.
Filter the query to only include matches where Barcelona was the away team.
*/

-- Select matches where Barcelona was the away team
SELECT  
	m.date,
	t.team_long_name AS opponent,
	CASE WHEN m.home_goal < m.away_goal THEN 'Barcelona win!'
        WHEN m.home_goal > m.away_goal THEN 'Barcelona loss :(' 
        ELSE 'Tie' END AS outcome
FROM matches_spain AS m
-- Join teams_spain to matches_spain
LEFT JOIN teams_spain AS t 
ON m.hometeam_Id = t.team_api_Id
WHERE m.awayteam_Id = 8634;



/* In CASE of rivalry
Barcelona and Real Madrid have been rival teams for more than 80 years. Matches between these two teams are given the name El Clásico (The Classic). In this exercise, you will query a list of matches played between these two rivals.

You will notice in Step 2 that when you have multiple logical conditions in a CASE statement, you may quickly end up with a large number of WHEN clauses to logically test every outcome you are interested in. It's important to make sure you don't accidentally exclude key information in your ELSE clause.

In this exercise, you will retrieve information about matches played between Barcelona (id = 8634) and Real Madrid (id = 8633). Note that the query you are provided with already identifies the Clásico matches using a filter in the WHERE clause.

Instructions 1/2
Complete the first CASE statement, identifying Barcelona or Real Madrid as the home team using the hometeam_id column.
Complete the second CASE statement in the same way, using awayteam_id.
Instructions 2/2
Construct the final CASE statement identifying who won each match. Note there are 3 possible outcomes, but 5 conditions that you need to identify.
Fill in the logical operators to identify Barcelona or Real Madrid as the winner.
*/

SELECT 
	date,
	-- Identify the home team as Barcelona or Real Madrid
	CASE WHEN hometeam_Id = 8634 THEN 'FC Barcelona' 
        ELSE 'Real Madrid CF' END AS home,
    -- Identify the away team as Barcelona or Real Madrid
	CASE WHEN awayteam_Id = 8634 THEN 'FC Barcelona' 
        ELSE 'Real Madrid CF' END AS away
FROM matches_spain
WHERE (awayteam_id = 8634 OR hometeam_id = 8634)
      AND (awayteam_id = 8633 OR hometeam_id = 8633);


SELECT 
	date,
	CASE WHEN hometeam_id = 8634 THEN 'FC Barcelona' 
         ELSE 'Real Madrid CF' END as home,
	CASE WHEN awayteam_id = 8634 THEN 'FC Barcelona' 
         ELSE 'Real Madrid CF' END as away,
	-- Identify all possible match outcomes
	CASE WHEN home_goal > away_goal AND hometeam_id = 8634 THEN 'Barcelona win!'
        WHEN home_goal > away_goal AND hometeam_id = 8633 THEN 'Real Madrid win!'
        WHEN home_goal < away_goal AND awayteam_id = 8634 THEN 'Barcelona win!'
        WHEN home_goal < away_goal AND awayteam_id = 8633 THEN 'Real Madrid win!'
        ELSE 'Tie!' END AS outcome
FROM matches_spain
WHERE (awayteam_id = 8634 OR hometeam_id = 8634)
      AND (awayteam_id = 8633 OR hometeam_id = 8633);



/* Filtering your CASE statement
Let's generate a list of matches won by Italy's Bologna team! There are quite a few additional teams in the two tables, so a key part of generating a usable query will be using your CASE statement as a filter in the WHERE clause.

CASE statements allow you to categorize data that you're interested in -- and exclude data you're not interested in. In order to do this, you can use a CASE statement as a filter in the WHERE statement to remove output you don't want to see.

Here is how you might set that up:

SELECT *
FROM table
WHERE 
    CASE WHEN a > 5 THEN 'Keep'
         WHEN a <= 5 THEN 'Exclude' END = 'Keep';
In essence, you can use the CASE statement as a filtering column like any other column in your database. The only difference is that you don't alias the statement in WHERE.

Instructions 1/3
Identify Bologna's team ID listed in the teams_italy table by selecting the team_long_name and team_api_id.
Instructions 2/3
Select the season and date that a match was played.
Complete the CASE statement so that only Bologna's home and away wins are identified.
*/

-- Select team_long_name and team_api_id from team
SELECT
	team_long_name,
	team_api_id
FROM teams_Italy
-- Filter for team long name
WHERE team_long_name = 'Bologna';


-- Select the season and date columns
SELECT 
	season,
	date,
    -- Identify when Bologna won a match
	CASE WHEN hometeam_id = 9857
        AND home_goal > away_goal 
        THEN 'Bologna Win'
		WHEN awayteam_id = 9857
        AND away_goal > home_goal 
        THEN 'Bologna Win' 
		END AS outcome
FROM matches_italy;

-- Select the season, date, home_goal, and away_goal columns
SELECT 
	season,
    date,
	home_goal,
	away_goal
FROM matches_italy
WHERE 
-- Exclude games not won by Bologna
	CASE WHEN hometeam_id = 9857 AND home_goal > away_goal THEN 'Bologna Win'
		WHEN awayteam_id = 9857 AND away_goal > home_goal THEN 'Bologna Win' 
		END IS NOT NULL;



/* COUNT using CASE WHEN
Do the number of soccer matches played in a given European country differ across seasons? We will use the European Soccer Database to answer this question.

You will examine the number of matches played in 3 seasons within each country listed in the database. This is much easier to explore with each season's matches in separate columns. Using the country and unfiltered match table, you will count the number of matches played in each country during the 2012/2013, 2013/2014, and 2014/2015 match seasons.

Instructions 1/2
Create a CASE statement that identifies the id of matches played in the 2012/2013 season. Specify that you want ELSE values to be NULL.
Wrap the CASE statement in a COUNT function and group the query by the country alias.
 */

SELECT 
	c.name AS country,
    -- Count games from the 2012/2013 season
	COUNT(CASE WHEN m.season = '2012/2013' 
        	THEN m.id ELSE NULL END) AS matches_2012_2013
FROM country AS c
LEFT JOIN match AS m
ON c.id = m.country_id
-- Group by country name alias
GROUP BY country;


SELECT 
	c.name AS country,
    -- Count matches in each of the 3 seasons
	COUNT(CASE WHEN m.season = '2012/2013' THEN m.id END) AS matches_2012_2013,
	COUNT(CASE WHEN m.season = '2013/2014' THEN m.id END) AS matches_2013_2014,
	COUNT(CASE WHEN m.season = '2014/2015' THEN m.id END) AS matches_2014_2015
FROM country AS c
LEFT JOIN match AS m
ON c.id = m.country_id
-- Group by country name alias
GROUP BY country;




/* COUNT and CASE WHEN with multiple conditions
In R or Python, you have the ability to calculate a SUM of logical values (i.e., TRUE/FALSE) directly. In SQL, you have to convert these values into 1 and 0 before calculating a sum. This can be done using a CASE statement.

There's one key difference when using SUM to aggregate logical values compared to using COUNT in the previous exercise --

Your goal here is to use the country and match table to determine the total number of matches won by the home team in each country during the 2012/2013, 2013/2014, and 2014/2015 seasons.

Instructions
Create 3 CASE statements to "count" matches in the '2012/2013', '2013/2014', and '2014/2015' seasons, respectively.
Have each CASE statement return a 1 for every match you want to include, and a 0 for every match to exclude.
Wrap the CASE statement in a SUM to return the total matches played in each season.
Group the query by the country name alias.
*/

SELECT 
	c.name AS country,
    -- Sum the total records in each season where the home team won
	SUM(CASE WHEN m.season = '2012/2013' AND m.home_goal > m.away_goal 
        THEN 1 ELSE 0 END) AS matches_2012_2013,
 	SUM(CASE WHEN m.season = '2013/2014' AND m.home_goal > m.away_goal 
        THEN 1 ELSE 0 END) AS matches_2013_2014,
	SUM(CASE WHEN m.season = '2014/2015' AND m.home_goal > m.away_goal 
        THEN 1 ELSE 0 END) AS matches_2014_2015
FROM country AS c
LEFT JOIN match AS m
ON c.id = m.country_id
-- Group by country name alias
GROUP BY country;




/* Calculating percent with CASE and AVG
CASE statements will return any value you specify in your THEN clause. This is an incredibly powerful tool for robust calculations and data manipulation when used in conjunction with an aggregate statement. One key task you can perform is using CASE inside an AVG function to calculate a percentage of information in your database.

Here's an example of how you set that up:

AVG(CASE WHEN condition_is_met THEN 1
         WHEN condition_is_not_met THEN 0 END)
With this approach, it's important to accurately specify which records count as 0, otherwise your calculations may not be correct!

Your task is to examine the number of wins, losses, and ties in each country. The matches table is filtered to include all matches from the 2013/2014 and 2014/2015 seasons.

Instructions 1/3
Create 3 CASE statements to COUNT the total number of home team wins, away team wins, and ties, which will allow you to examine the total number of records.
Instructions 2/3
Calculate the percentage of matches tied using a CASE statement inside AVG.
Fill in the logical operators for each statement. Alias your columns as ties_2013_2014 and ties_2014_2015, respectively.
*/

SELECT 
    c.name AS country,
    -- Count the home wins, away wins, and ties in each country
	COUNT(CASE WHEN m.home_goal > m.away_goal THEN m.id 
        END) AS home_wins,
	COUNT(CASE WHEN m.home_goal < m.away_goal THEN m.id 
        END) AS away_wins,
	COUNT(CASE WHEN m.home_goal = m.away_goal THEN m.id 
        END) AS ties
FROM country AS c
LEFT JOIN matches AS m
ON c.id = m.country_id
GROUP BY country;


SELECT 
	c.name AS country,
    -- Calculate the percentage of tied games in each season
	AVG(CASE WHEN m.season='2013/2014' AND m.home_goal = m.away_goal THEN 1
			WHEN m.season='2013/2014' AND m.home_goal != m.away_goal THEN 0
			END) AS ties_2013_2014,
	AVG(CASE WHEN m.season='2014/2015' AND m.home_goal = m.away_goal THEN 1
			WHEN m.season='2014/2015' AND m.home_goal != m.away_goal THEN 0
			END) AS ties_2014_2015
FROM country AS c
LEFT JOIN matches AS m
ON c.id = m.country_id
GROUP BY country;


SELECT 
	c.name AS country,
    -- Round the percentage of tied games to 2 decimal points
	ROUND(AVG(CASE WHEN m.season='2013/2014' AND m.home_goal = m.away_goal THEN 1
			 WHEN m.season='2013/2014' AND m.home_goal != m.away_goal THEN 0
			 END),2) AS pct_ties_2013_2014,
	ROUND(AVG(CASE WHEN m.season='2014/2015' AND m.home_goal = m.away_goal THEN 1
			 WHEN m.season='2014/2015' AND m.home_goal != m.away_goal THEN 0
			 END),2) AS pct_ties_2014_2015
FROM country AS c
LEFT JOIN matches AS m
ON c.id = m.country_id
GROUP BY country;