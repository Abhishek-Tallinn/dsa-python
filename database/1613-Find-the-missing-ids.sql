-- Problem: Leetcode 1613 - Find the missing IDs
-- Difficulty: Medium
-- Link: https://leetcode.com/find-the-missing-ids/description/
-- Approach: This is a good recursive CTE question where the numbers CTE refers itself and 
-- therefore becomes recursive and hence we are able to generate a list of numbers first upto the max customer_id
-- and then select the ids which dont occur in this generated table.


with recursive 
mx as (
    select max(customer_id) as max_id
    from Customers
),
numbers AS (


    SELECT 1 AS n
    UNION ALL

    SELECT n + 1
    FROM numbers,mx
    WHERE n < mx.max_id
)

SELECT n as ids
FROM numbers
where n NOT in (select customer_id from Customers);