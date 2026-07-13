-- Problem: Leetcode 1565 - Unique orders and customers per month
-- Difficulty: Easy
-- Link: https://leetcode.com/unique-orders-and-customers-per-month/description/
-- Approach: We make a derived table with formatted month substring which we already filter the rows with lower value invoice
-- then we join it back to the main table and filter what we need

select t.mon as month, count(*) as order_count, count(DISTINCT customer_id) as customer_count
from Orders o
join (
    select o1.order_id,SUBSTRING(o1.order_date,1,7) as mon
    from Orders o1
    where o1.invoice>20
) t
    on o.order_id = t.order_id
group by t.mon;