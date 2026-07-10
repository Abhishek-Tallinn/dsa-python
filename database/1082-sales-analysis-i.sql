-- Problem: Leetcode 1082 - Sales analysis - I
-- Difficulty: Easy
-- Link: https://leetcode.com/problems/sales-analysis-i/description/
-- Approach: We group by seller_id and filter by SUM of the price values and we calculate max of that price in a separate subquery and equate them.

select s.seller_id 
FROM Sales s
group by seller_id
having SUM(price) = 
    ( 
        select MAX(p)
        FROM (
            select s1.seller_id,SUM(s1.price) as p
            from Sales s1
            group by seller_id
        ) t

    );