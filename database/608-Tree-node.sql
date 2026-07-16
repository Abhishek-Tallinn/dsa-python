-- Problem: Leetcode 608 - Tree Node
-- Difficulty: Medium
-- Link: https://leetcode.com/problems/tree-node/description/
-- Approach: For clarity we make a cleaned_pid table removing the null values and then we make our selection.
-- if the pid is null we know its root and if not then we check if node is occurs in p_id column meaning that its the parent of some nood
-- in which case is inner node else it is a leaf node.
-- here we have to remember that IN operator take a subquery based list of values and cannot take a 
-- common table expression directly. its not possible to do that


with cleaned_pid as (
    select p_id from Tree
    where p_id IS NOT NULL
)

select t.id, 
        CASE
         when p_id IS NULL then 'Root'
         when t.id IN (select p_id from cleaned_pid) then 'Inner'
         ELSE 'Leaf'
         END as type
from Tree t;