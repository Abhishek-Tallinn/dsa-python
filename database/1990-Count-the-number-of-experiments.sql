-- Problem: Leetcode 1990 - Count the number of experiments
-- Difficulty: Medium
-- Link: https://leetcode.com/count-the-number-of-experiments/description/
-- Approach: This is a unique CTE approach as we have enums and the each enum value should figure 
-- for all possible levels of Exp. Then we can perform the SQL query to cross join exp with P and then
-- left join this to experiments table on the platform and exp name and just COUNT the distinct
-- experiment_id which automatically excludes null values

WITH
P AS (
    SELECT 'Android' AS platform
    UNION
    SELECT 'IOS'
    UNION
    SELECT 'Web'
),
Exp AS (
    SELECT 'Reading' AS experiment_name
    UNION
    SELECT 'Sports'
    UNION
    SELECT 'Programming'
)

SELECT
    p.platform,
    e.experiment_name,
    COUNT(ex.experiment_id) AS num_experiments
FROM P p
CROSS JOIN Exp e
LEFT JOIN Experiments ex
on p.platform = ex.platform and ex.experiment_name = e.experiment_name
GROUP BY platform, experiment_name;
    
/*
select temp2.platform,temp2.experiment_name,COUNT(experiment_id) 
as num_experiments from ( select DISTINCT e1.platform ,temp.experiment_name 
from Experiments e1 cross join ( select DISTINCT e2.experiment_name from Experiments e2 ) temp ) 
temp2 
left join Experiments e3 
on e3.platform = temp2.platform and e3.experiment_name = temp2.experiment_name 
group by temp2.platform,temp2.experiment_name;
*/