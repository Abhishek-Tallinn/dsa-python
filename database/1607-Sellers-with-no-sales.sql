-- Problem: Leetcode 1607 - Sellers with no sales
-- Difficulty: Easy
-- Link: https://leetcode.com/sellers-with-no-sales/description/
-- Approach: We join seller table with orders table and then we group by each seller and count within each
-- group that how many sales they have in 2020. if its 0 then that means they made no sales in 2020.
-- then at the end we order by seller_name

select s.seller_name 
from Seller s
left join Orders o
    ON s.seller_id = o.seller_id
group by s.seller_id
having COUNT(case when sale_date BETWEEN '2020-01-01' and '2020-12-31' then 1 end) = 0
order by seller_name ASC;