-- Problem: Leetcode 1045 - Customers who bought all products
-- Difficulty: Medium
-- Link: https://leetcode.com/problems/customers-who-bought-all-products/description/
-- Approach: If a customer bought all the products then after the group by call, if a customer group distinct product key count
-- is equal to their total product count in the product table then we can say that the customer
-- has indeed bought all the products

select customer_id 
from Customer 
group by customer_id
having COUNT(DISTINCT product_key) = (select COUNT(DISTINCT product_key) from Product);