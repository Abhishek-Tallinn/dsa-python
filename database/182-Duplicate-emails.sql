-- Problem: Leetcode 182 - Duplicate Emails
-- Difficulty: Easy
-- Link: https://leetcode.com/problems/duplicate-emails/description/
-- Approach: we use GROUP BY and HAVING to find emails that appear more than once in the Person table


SELECT email 
FROM Person
GROUP BY email
HAVING COUNT(*) > 1;