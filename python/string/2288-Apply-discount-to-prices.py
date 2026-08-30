# Problem: Leetcode 2288 - Apply discount to prices
# Difficulty: Medium
# Link: https://leetcode.com/problems/apply-discount-to-prices/description/
# Time Complexity: O(n) 
# Space Complexity: O(n) 
# Approach: We split sentence into words and if we find a word that starts with $ and has a valid value
# then we simply calculate its new price and replace the element in words list. We format each new price to 2 
# decimal places before adding it. Then we join words and return it.

class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        words = sentence.split(" ")
        for i,word in enumerate(words):
            if word[0]=='$':
                try:
                    curr_price = int(word[1:])
                except ValueError:
                    continue
                new_price = curr_price - ((curr_price * discount) / 100)
                words[i] = '$' + f"{new_price:.2f}"
                
        return ' '.join(words)