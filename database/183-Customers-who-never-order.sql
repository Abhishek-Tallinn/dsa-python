-- Problem: Leetcode 183 - Customers Who Never Order
-- Difficulty: Easy
-- Link: https://leetcode.com/problems/customers-who-never-order/description/
-- Approach: we use a LEFT JOIN to find customers who have no corresponding order in the orders table by filter on NULL

SELECT c.name as Customers
FROM CUSTOMERS c
left join Orders o
on c.id = o.customerId
where o.id IS NULL;