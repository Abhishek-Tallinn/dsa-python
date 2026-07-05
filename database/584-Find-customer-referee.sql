-- Problem: Leetcode 584 - Find Customer Referee
-- Difficulty: Easy
-- Link: https://leetcode.com/problems/find-customer-referee/description/
-- Approach: we filter customers where referee_id is NULL or not equal to 2.


SELECT c.name
FROM Customer c
where c.referee_id IS NULL or c.referee_id <> 2;