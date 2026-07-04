-- Problem: Leetcode 595 - Big Countries
-- Difficulty: Easy
-- Link: https://leetcode.com/problems/big-countries/description/
-- Approach: we select the name, population, and area from the World table and filter for countries with an area of at least 3,000,000 or a population of at least 25,000,000.
-- Simple query


select w.name,w.population,w.area 
from World w
where w.area>=3000000 or w.population >= 25000000;