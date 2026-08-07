-- Problem: Leetcode 1543 - Fix Product Name Format
-- Difficulty: Easy
-- Link: https://leetcode.com/problems/fix-product-name-format/description/
-- Approach: We use LOWER and TRIM functions to standardize the product names and then group by the standardized names and sale dates.
-- There are two approaches here with CTE and also the direct appraoch. we need to remember that in strict mode we need to group by everything that we select by


with lt as (
select LOWER(TRIM(product_name)) as product_name, substring(sale_date,1,7) as sale_date
from Sales
)

select product_name, sale_date, count(*) as total
from lt
group by product_name, sale_date
order by product_name, sale_date;



--select LOWER(TRIM(s.product_name)) as product_name, substring(s.sale_date,1,7) as sale_date, COUNT(*) as total
--from Sales s
--group by LOWER(TRIM(s.product_name)),substring(s.sale_date,1,7)
--order by LOWER(TRIM(s.product_name)), sale_date;
