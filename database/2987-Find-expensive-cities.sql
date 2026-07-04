-- Problem: Leetcode 2987 - Find expensive cities
-- Difficulty: Easy
-- Link: https://leetcode.com/problems/find-expensive-cities/description/
-- Approach: we select the city from the Listings table and group by city to get the average price.
-- Then we filter the results to only include cities with an average price greater than the overall average price 
-- by evaluating national average with a subquery.

SELECT city
from Listings 
group by city
having AVG(price) > (
    select avg(price) 
    from Listings 
    )
order by city;