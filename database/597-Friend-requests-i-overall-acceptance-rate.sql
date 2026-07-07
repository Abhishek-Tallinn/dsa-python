-- Problem: Leetcode 597 - Friend requests I - Overall Acceptance Rate
-- Difficulty: Easy
-- Link: https://leetcode.com/problems/friend-requests-i-overall-acceptance-rate/description/
-- Approach: We use coalesce to return 0 in case of null values and we use a subquery in FROM to return a temporary tables which is
-- use to calculate the acceptance rate

SELECT COALESCE(ROUND(accepted/requests,2),0) as accept_rate
FROM (
    SELECT
    (SELECT COUNT(DISTINCT requester_id,accepter_id) from RequestAccepted) as accepted,
    (SELECT COUNT(DISTINCT sender_id,send_to_id) from FriendRequest) as requests
    ) t;