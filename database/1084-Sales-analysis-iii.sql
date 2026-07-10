-- Problem: Leetcode 1084 - Sales analysis - III
-- Difficulty: Easy
-- Link: https://leetcode.com/problems/sales-analysis-iii/description/
-- Approach: We select product id and name from a join and in the join we join a derived sales tables where we already filter out the 
-- products who have had any sale outside of the window

select p.product_id,p.product_name
from Product p
join
    (
        select product_id
        from Sales 
        group by product_id
        having 
            count(case when sale_date BETWEEN '2019-01-01' and '2019-03-31' then 1 end) > 0 and
            count(case when sale_date < '2019-01-01' or sale_date > '2019-03-31' then 1 end) = 0 

    ) temp
on p.product_id = temp.product_id;