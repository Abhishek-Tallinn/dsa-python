-- Problem: Leetcode 1174 - Immediate food delivery II
-- Difficulty: Medium
-- Link: https://leetcode.com/problems/immediate-food-delivery-ii/description/
-- Approach: We first make a derived table with only the first orders of a customer which we join
-- back to the main table on both customer id and order date to get a final table which only has 
-- customer_id,order_date and customer_pref_delivery date and now this total derived table becomes our base
-- and from this we select the rows where order_Date = customer_pref_delivery date and divide
-- by the total rows in the table

select ROUND(COUNT(CASE when order_date = customer_pref_delivery_date then 1 end)/COUNT(DISTINCT customer_id)*100,2) as immediate_percentage
from (
    select d1.customer_id,d1.order_date, d1.customer_pref_delivery_date
    from Delivery d1
    join (
        select d2.customer_id,MIN(order_date) as first_order
        from Delivery d2
        group by customer_id
    ) t
    on d1.customer_id = t.customer_id and d1.order_date = t.first_order
) t2