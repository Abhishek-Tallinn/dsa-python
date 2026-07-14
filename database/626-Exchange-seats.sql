-- Problem: Leetcode 626 - Exchange seats
-- Difficulty: Medium
-- Link: https://leetcode.com/problems/exchange-seats/description/
-- Approach: We just select the students based on id matching. whenever selection criteria varies
-- think abut the case approach with or without subqueries. Easy once you see it


select s1.id, CASE
            WHEN s1.id%2=1 and id!=(select count(*) from seat) THEN (select s2.student from Seat s2 where s2.id = s1.id+1)
            WHEN s1.id%2=0 THEN (select s3.student from Seat s3 where s3.id = s1.id-1)
            ELSE s1.student
           END as student
from Seat s1;

-- too many subqueries but still fast. experience person will perform a join