-- Write your MySQL query statement below
-- Problem: Leetcode 1098 - Unpopular books
-- Difficulty: Medium
-- Link: https://leetcode.com/problems/unpopular-books/description/
-- Approach: We use a left join and in the join condition we already filter books within last year therby keeping the books that
--dont figure in it and then we group by and we do having IFNULL(SUM(o.quantity),0) < 10 to change null to zero and compare with 10.

SELECT b.book_id, b.name
FROM Books b
LEFT JOIN Orders o 
    ON b.book_id = o.book_id 
    AND o.dispatch_date BETWEEN '2018-06-23' AND '2019-06-23'
WHERE b.available_from < '2019-05-23'
GROUP BY b.book_id, b.name
HAVING IFNULL(SUM(o.quantity), 0) < 10;

/*
select b.book_id,b.name
from Books b
left join (
    select book_id
    from Orders 
    where dispatch_date < '2018-06-23' or dispatch_date IS NULL
) t1 on b.book_id = t1.book_id
left join (
    select book_id
    from Orders 
    where dispatch_date between '2018-06-23' and '2019-06-23'
    group by order_id
    having SUM(quantity)<10
) t2 on b.book_id = t2.book_id
where b.available_from < '2019-05-23'
AND (t1.book_id IS NOT NULL OR t2.book_id IS NOT NULL)
group by b.book_id;
*/