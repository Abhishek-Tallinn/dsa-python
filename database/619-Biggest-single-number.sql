-- Problem: Leetcode 619 - Biggest Single Number
-- Difficulty: Easy
-- Link: https://leetcode.com/problems/biggest-single-number/description/
-- Approach: We need to find the largest number that appears only once in the table.
-- This can be done by grouping the numbers and filtering for those that appear exactly once, then selecting the maximum.
-- we wrap it in a subquery to return null if number not found



select(
    select num 
    from MyNumbers
    group by num
    having COUNT(*)=1
    order by num DESC
    limit 1 ) as num;
