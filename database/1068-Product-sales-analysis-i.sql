-- Problem: Leetcode 1068 - Product sales analysis
-- Difficulty: Easy
-- Link: https://leetcode.com/problems/product-sales-analysis/description/
-- Approach: Since we need to produce output values for each sales_id we can left join with product on 
-- product id and return the values.

select p.product_name,s.year,s.price 
from sales s
left join Product p
ON s.product_id = p.product_id;