-- Problem: Leetcode 180 - Consecutive Numbers
-- Difficulty: Medium
-- Link: https://leetcode.com/problems/consecutive-numbers/description/
-- Approach: we use joins to find consecutive numbers in the Logs table
-- as we want to identify numbers that appear in three consecutive rows. so we two self joins
-- and then since we join on one id count less then we can see if id 1 and id 2 and id 3 numbers are same or any id sequence.




SELECT DISTINCT l1.num as ConsecutiveNums
FROM Logs l1
JOIN Logs l2
    ON l1.id = l2.id-1
JOIN Logs l3
    ON l2.id = l3.id-1
WHERE l1.num=l2.num
AND l2.num = l3.num;