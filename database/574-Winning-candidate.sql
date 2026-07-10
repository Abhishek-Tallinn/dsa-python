-- Problem: Leetcode 574 - Winning candidate
-- Difficulty: Medium
-- Link: https://leetcode.com/problems/winning-candidate/description/
-- Approach: We selct name from Candidate table but join a derived table which only return the top candidate with most votes 
-- then we join on the foreign key and this gives us the name of the candidate.

select c.name as name
from Candidate c
join (
    select candidateId, COUNT(*) as votes
    from Vote
    group by candidateId
    order by votes DESC
    limit 1
) t
on c.id = t.candidateId;