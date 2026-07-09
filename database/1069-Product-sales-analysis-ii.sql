-- Problem: Leetcode 1069 - Product sales analysis - ii
-- Difficulty: Easy
-- Link: https://leetcode.com/problems/product-sales-analysis-ii/description/
-- Approach: We simply group by the product id and sum the total quantity of each to return the total

select s.product_id, sum(s.quantity) as total_quantity
from Sales s
group by product_id;