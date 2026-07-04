-- Problem: Leetcode 596 - Class with at least 5 students
-- Difficulty: Easy
-- Link: https://leetcode.com/problems/class-with-at-least-5-students/description/
-- Approach: we select the class from the Courses table and group by class to get the count of students.
-- Then we filter the results to only include classes with a count of at least 5 students.

SELECT class from Courses
GROUP BY class
HAVING COUNT(*)>4;