-- Problem: Leetcode 627 - Swap Salary
-- Difficulty: Easy
-- Link: https://leetcode.com/problems/swap-salary/description/
-- Approach: We use a CASE statement to swap the values of the sex column, changing 'm' to 'f' and 'f' to 'm'.


update Salary
set sex=
    CASE
        WHEN sex='m' THEN 'f'
        WHEN sex='f' THEN 'm'
        ELSE sex #for other values if we dont want to change
    END;