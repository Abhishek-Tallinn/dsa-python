-- Problem: Leetcode 178 - Rank Scores
-- Difficulty: Medium
-- Link: https://leetcode.com/problems/rank-scores/description/
-- Approach: we use a subquery to find the rank of each score in the Scores table
-- as we want to assign ranks to scores in descending order. so we use subquery to count the number of distinct values 
-- that are greater than or equal to the current score to determine its rank.


select s1.score, 
        ( SELECT COUNT(DISTINCT s2.score)
        FROM Scores s2
        WHERE s2.score>=s1.score
        ) AS 'rank'
FROM Scores s1
ORDER by s1.score DESC;