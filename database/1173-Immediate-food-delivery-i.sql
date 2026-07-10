-- Problem: Leetcode 1173 - Immediate food delivery I
-- Difficulty: Easy
-- Link: https://leetcode.com/problems/immediate-food-delivery-i/description/
-- Approach: We simply solve it directly by counting in select or by second method by using two scalar subqueries
-- where one subquery calculate immediate and total which each subquery returns and 
-- we use it to calculate percentage

select ROUND(100*COUNT(CASE when order_date=customer_pref_delivery_date then 1 END)/COUNT(*),2) as immediate_percentage
from Delivery;

/*scalar sub qeuery method - no derived table

select ROUND(immediate/total * 100,2) as immediate_percentage
from (
    select
    (select COUNT(*) from Delivery 
    where order_date = customer_pref_delivery_Date) as immediate,
    (select COUNT(*) from Delivery) as total
    ) t;
*/