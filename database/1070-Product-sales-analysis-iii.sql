-- Problem: Leetcode 1070 - Product sales analysis - III
-- Difficulty: Medium
-- Link: https://leetcode.com/problems/product-sales-analysis-iii/description/
-- Approach: We try the simple O(n^2) approach where we take each outer row and check it with subquery if the year matches to minimum or no which is causing TLE
-- So we use optimized appraoch where we make a derived table with the product id with the earliest year and we joing this table back to the original table to 
-- get the relevant quantity and price.

select s.product_id,s.year as first_year, s.quantity,s.price 
from Sales s
join (
    select s1.product_id,MIN(s1.year) as mi
    from Sales s1 
    group by product_id 
    ) first_sales
on s.product_id=first_sales.product_id and s.year = first_sales.mi;



/*
#works but O(n^2)
select s.product_id, s.year as first_year, s.quantity, s.price 
from sales s
where s.year = 
    ( 
        select MIN(s1.year) 
        from Sales s1
        where s1.product_id = s.product_id

    );
