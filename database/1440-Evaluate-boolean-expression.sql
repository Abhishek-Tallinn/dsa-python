-- Problem: Leetcode 1440 - Evaluate boolean expresssion
-- Difficulty: Medium
-- Link: https://leetcode.com/evaluate-boolean-expression/description/
-- Approach: We have to join the same table twice as we want both left and right values inside
-- the same row so that the boolean can be evaluated and to evaluate the boolean we 
-- use the CASE when and then and else syntax


SELECT
    e.left_operand,
    e.operator,
    e.right_operand,
    CASE
    WHEN e.operator = '>' AND lv.value > rv.value THEN 'true'
    WHEN e.operator = '<' AND lv.value < rv.value THEN 'true'
    WHEN e.operator = '=' AND lv.value = rv.value THEN 'true'
    ELSE 'false'
    END AS value
FROM Expressions e
LEFT JOIN Variables lv
    ON e.left_operand = lv.name
LEFT JOIN Variables rv
    ON e.right_operand = rv.name;