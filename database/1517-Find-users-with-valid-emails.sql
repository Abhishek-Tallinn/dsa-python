-- Problem: Leetcode 1517 - Find users with valid emails
-- Difficulty: Easy
-- Link: https://leetcode.com/find-users-with-valid-emails/description/
-- Approach: We simply use regex expression for matching the mail and since MYSQL is case insensitive by default,
-- we have to use a special check for the ending part as it has test case with COM

select *
from Users 
WHERE mail REGEXP '^[A-Za-z][A-Za-z0-9._-]*@leetcode\\.com$'
 and BINARY mail LIKE '%@leetcode.com';