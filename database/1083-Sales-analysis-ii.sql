-- Problem: Leetcode 1083 - Sales analysis - II
-- Difficulty: Easy
-- Link: https://leetcode.com/problems/sales-analysis-ii/description/
-- Approach: We group by seller_id and filter by SUM of the price values and we calculate max of that price in a separate subquery and equate them.

select s.buyer_id 
from Sales s
join Product p
on p.product_id = s.product_id
group by s.buyer_id 
having 
    SUM(product_name='S8') > 0
    AND SUM(product_name='iPhone') = 0;

-- cannot use count in filter as it will count the rows which
-- will include the 0 values also