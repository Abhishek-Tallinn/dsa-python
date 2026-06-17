# Problem: Leetcode 468 - Validate IP address
# Difficulty: Medium
# Link: https://leetcode.com/problems/validate-ip-address/description/
# Time Complexity: O(n) - where n is the length of the input address
# Space Complexity: O(n) as we split the input array
# Approach: Its a straight forward input validation problem where we just follow the constraints add add input validation checks

class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        def ipv4(ip:str)->str:
            values = ip.split(".")
            if len(values)!=4:
                return "Neither"
            for value in values:
                for char in value:
                    if not char.isdigit():
                        return "Neither"
                if not value or int(value)<0 or int(value)>255 or (len(value)>1 and value[0]=='0'):
                    return "Neither"
                
                
            return "IPv4"

        def ipv6(ip:str)->str:
            valid = {'a','A','b','B','c','C','d','D','e','E','f','F'}
            values = ip.split(":")
            if len(values)!=8:
                return "Neither"
            for value in values:
                if len(value)<1 or len(value)>4:
                    return "Neither"
                for char in value:
                    if (not char.isdigit()) and (not char in valid):
                        return "Neither"
                

            return "IPv6"
            

        for char in queryIP:
            if char==".":
                return ipv4(queryIP)
            elif char==":":
                return ipv6(queryIP)
        return "Neither"