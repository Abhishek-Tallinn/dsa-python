-- Problem: Leetcode 1241 - Number of comments per post
-- Difficulty: Easy
-- Link: https://leetcode.com/problems/number-of-comments-per-post/description/
-- Approach: We make a derived table with only those sub_id which are actually posts then we self join the main table
-- with a left join on sub_id = parent_id so that all posts which are parents meaning have a comment are filtered
-- and then from this we select the sub_id which are posts selected in first derived table
-- and use aggregation COUNT to count the distinct sub_id which are comments on these posts with these posts 
-- figuring as parent_id to these comments


select temp2.sub_id as post_id,COUNT(distinct temp2.comment_id) as number_of_comments
from 
(   
    select temp1.sub_id, s2.sub_id as comment_id
    from (
        select DISTINCT s1.sub_id
        from Submissions s1
        where s1.parent_id IS NULL
    ) as temp1
    left join Submissions s2
    ON temp1.sub_id = s2.parent_id
) as temp2
group by temp2.sub_id;