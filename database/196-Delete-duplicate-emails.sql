-- Problem: Leetcode 196 - Delete Duplicate Emails
-- Difficulty: Easy
-- Link: https://leetcode.com/problems/delete-duplicate-emails/description/
-- Approach: we use a self-join to identify duplicate emails and delete the rows with higher IDs. so only
-- the rows with first occurrence of the email will be kept in the Person table. we use the condition p1.id>p2.id to ensure that we only delete the duplicate rows with higher IDs.

DELETE p1 
from person p1
join person p2
on p1.email = p2.email
where p1.id>p2.id;