# Problem: Leetcode 506 - Relative Ranks
# Difficulty: Easy
# Link: https://leetcode.com/problems/relative-ranks/description/
# Time Complexity: O(n log n) due to sorting, where n is the number of scores
# Space Complexity: O(n) for the dictionary and result list
# Approach: We sort the scores in descending order and create a mapping from each score to its rank. Then we iterate through the original scores and assign the appropriate medal or rank based on the mapping.


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        ans = ['0']*len(score)
        d = {score:i for i,score in enumerate(sorted(score,reverse=True))}
        for i in range(len(score)):
            rank = d[score[i]]
            if rank==0:
                ans[i] = "Gold Medal"
            elif rank == 1:
                ans[i] = "Silver Medal"
            elif rank ==2:
                ans[i] = "Bronze Medal"
            else:
                ans[i] = str(rank+1)
        return ans