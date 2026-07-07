-- Problem: Leetcode 1113 - Reported Posts
-- Difficulty: Easy
-- Link: https://leetcode.com/problems reported-posts/description/
-- Approach: We select the extra column as report_reason and count the distinct post_ids for each report reason from the Actions table, filtering for reports on a specific date.

select extra as report_reason, COUNT(DISTINCT post_id) as report_count
from Actions
where action_date = '2019-07-04' and action='report' and extra IS NOT NULL
group by extra;