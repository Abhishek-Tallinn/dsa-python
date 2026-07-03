-- Problem: Leetcode 586 - Customer placing the largest number of orders
-- Difficulty: Easy
-- Link: https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/description/
-- Approach: we just select the customer_number from the tables and perform a group by on the customer number to get the count.
-- Then we order the result in descending order with the count and return the top result.

select customer_number
from Orders 
group by customer_number
order by count(*) DESC
limit 1;