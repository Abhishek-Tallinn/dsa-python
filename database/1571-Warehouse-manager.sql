-- Problem: Leetcode 1571 - Warehouse manager
-- Difficulty: Easy
-- Link: https://leetcode.com/warehouse-manager/description/
-- Approach: We make a derived table with product_id and the total volumne of each product which 
-- we then join with warehouse table and group every warehouse and then return the name and the 
-- mathematical SUM(vol*units) from the joint table

select w.name as warehouse_name, SUM(vol*units) as volume
from Warehouse w
join 
    ( 
        select p1.product_id, (p1.Width*p1.Length*p1.Height) as vol
        from Products p1    
    ) temp
    ON w.product_id = temp.product_id
group by w.name;