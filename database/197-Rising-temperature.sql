-- Problem: Leetcode 197 - Rising Temperature
-- Difficulty: Easy
-- Link: https://leetcode.com/problems/rising-temperature/description/
-- Approach: we use a self-join to identify rows with rising temperatures compared to the previous day.
-- this is dont by joining on date with interval of 1 day and comparing temperatures of the w1 table with the w table. we select the ids of the rows in the w1 table where the temperature is greater than the temperature in the w table.

select w1.id 
from Weather w
join Weather w1
ON w1.recordDate = DATE_ADD(w.recordDate, INTERVAL 1 DAY)
where w1.temperature > w.temperature;