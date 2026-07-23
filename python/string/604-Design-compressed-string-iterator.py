# Problem: Leetcode 604 - Design compressed string iterator
# Difficulty: Easy
# Link: https://leetcode.com/problems/design-compressed-string-iterator/description/
# Time Complexity: O(n) - passing over each character of decompressed string
# Space Complexity: O(1)
# Approach: We decompress the string but limit it to the maximum of calls to be made to next and has next
# and then we return the next element of the decompressed string in sequence

class StringIterator:

    def __init__(self, compressedString: str):
        self.cs = self.constructString(compressedString)
        self.i = 0

    def constructString(self,s):
        res = ""
        j = 0
        while j < len(s):
            if s[j].isdigit():
                char = s[j-1]
                start = j
                while j< len(s) and s[j].isdigit():
                    j+=1
                mul = int(s[start:j])
                if mul > 100:
                    mul = 100
                res += char*mul
            j+=1
        return ''.join(res)

    def next(self) -> str:
        if not self.hasNext():
            return ' '
        self.i+=1
        return self.cs[self.i-1]


    def hasNext(self) -> bool:
        return self.i!=len(self.cs)
        


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()