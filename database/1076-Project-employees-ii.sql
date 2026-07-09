-- Problem: Leetcode 1076 - Project employees - II
-- Difficulty: Easy
-- Link: https://leetcode.com/problems/product-employees-ii/description/
-- Approach: We first group by project id and takes it count which we compare to a derived table which produces a list of count 
-- and the project_id and then we take maximum of cnt from the table which we compare to our original having filter

select p.project_id 
from Project p
group by project_id
having count(*) = 
      ( 
        select max(cnt)
        FROM (
            select project_id,count(*) as cnt
            from Project 
            group by project_id
        )t 
    );