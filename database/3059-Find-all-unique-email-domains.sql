-- Problem: Leetcode 3059 - Find all unique email domains
-- Difficulty: Easy
-- Link: https://leetcode.com/problems/find-all-unique-email-domains/description/
-- Approach: we extract the email domain from each email address and count the occurrences.
-- we can use a direct approach by calculating substring at each stage but we use a subquery so that the result of filter domain and the extension is available as an alias to 
-- our outer query. Also at the end we order the result by email domain to get the final output.


SELECT email_domain,COUNT(*) as `count`
from    (
        SELECT 
            SUBSTRING(email from POSITION('@' in email)+1) as email_domain,
            SUBSTRING(email from POSITION('.' in email)+1) as extension
        FROM Emails
    ) t
where extension = 'com'
group by email_domain
order by email_domain;


--SELECT SUBSTRING(email from POSITION('@' IN EMAIL)+1) as email_domain, COUNT(*) as count
--FROM Emails
--where SUBSTRING(email from POSITION('.' IN EMAIL)+1) = 'com'
--GROUP BY SUBSTRING(email from POSITION('@' IN EMAIL)+1);