-- Problem: Leetcode 607 - Sales Person
-- Difficulty: Easy
-- Link: https://leetcode.com/problems/sales-person/description/
-- Approach: we select the name from the SalesPerson table and exclude those who have made sales to the company named 'RED'.
-- The reason that we cannot have join Salesperson with orders is that we even need to include those salesperson who have no sales at all
-- because it means thaty they have not sold to company RED. so we use a subquery to get the sales_id of those who have sold to company RED and then exclude them from the SalesPerson table.

SELECT sp.name
FROM SalesPerson sp
WHERE sales_id NOT IN 
    (
        SELECT o.sales_id 
        FROM Orders o
        JOIN Company c
            ON o.com_id = c.com_id
        WHERE c.name='RED'
    );
#so everyone who sold to company RED are excluded