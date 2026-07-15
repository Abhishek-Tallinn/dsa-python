-- Problem: Leetcode 585 - Investments in 2016
-- Difficulty: Medium
-- Link: https://leetcode.com/problems/Investments-in-2016/description/
-- Approach: we make a derived table with lat,lon repeat rows removed and join it to main table
-- and then we use this final dervied table to calculate sum of investments in 2016 only from 
-- those rows where tiv 2015 is not unique

 
select ROUND(SUM(temp2.tiv_2016),2) as tiv_2016
from (
    select i2.tiv_2015,i2.tiv_2016 
    from Insurance i2
    join (
        select i.pid,i.tiv_2015,i.tiv_2016
        from Insurance i
        group by lat,lon
        having COUNT(*)=1
        ) temp
        on i2.pid = temp.pid
    ) temp2
where temp2.tiv_2015 IN
( select tiv_2015
from Insurance
group by tiv_2015
having COUNT(*)>1)