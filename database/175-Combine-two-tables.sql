-- Problem: Leetcode 175 - Combine two tables
-- Difficulty: Easy
-- Link: https://leetcode.com/problems/combine-two-tables/description/
-- Approach: we use a LEFT JOIN to combine the Person and Address tables based on the personID 
-- to get the names and city and state



SELECT p.FirstName,p.LastName, a.city,a.state 
FROM Person as p
LEFT JOIN Address as a
on p.personID = a.personID;