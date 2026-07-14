-- Problem: Leetcode 2356 - Number of unique subject taught by each teacher
-- Difficulty: Easy
-- Link: https://leetcode.com/number-of-unique-subject-taught-by-each-teacher/description/
-- Approach: Just group by teacher and count the distinct subjects

select teacher_id, COUNT(DISTINCT subject_id) as cnt
from Teacher
group by teacher_id;