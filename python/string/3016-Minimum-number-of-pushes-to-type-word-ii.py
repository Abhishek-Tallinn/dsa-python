from collections import Counter
class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        d = Counter(word)
        s_d = [k for k,v in sorted(d.items(),key = lambda x:x[1], reverse=True)]
        total = 0
        counter = 0
        mul = 1
        for idx,char in enumerate(s_d):
            total += d[char] * mul
            counter+=1
            if counter%8==0:
                mul+=1
        return total