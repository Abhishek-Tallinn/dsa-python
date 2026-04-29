# Problem: Leetcode 293 - Flip Game
# Difficulty: Easy
# Link: https://leetcode.com/problems/flip-game/description/
# Time Complexity: O(n)
# Space Complexity: O(n)
# Approach: For O(n) appraoch we can make an array by splitting the string into stack array and then iterate over string and when two consecutive
# '+' characters are found, we can flip them to '-' and add the new flipped state to stack and add the stack to the possible states. After that we can flip the stack indices back to '+' for next iterations.
# O(n^2) approach just modified the string by sliving and concatenating which makes a new string and then appending it possible states.
# While time complexity is O(n^2) for second approach, the space complexity is O(1) as no new data strcture is used. 
# In first approach, time complexity is O(n) but space complexity is O(n) as we are using a stack to store the characters of the string. 

class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        #O(n) solution
        if len(currentState)==1:
            return []
        possible_states = []
        stack = [char for char in currentState]
        for idx in range(len(currentState)-1):
            if currentState[idx]=="+" and currentState[idx+1]=="+":
                stack[idx]="-"
                stack[idx+1]="-"
                possible_states.append(''.join(stack))
                stack[idx]="+"
                stack[idx+1]="+"
        return possible_states
        #O(n^2) solution
        '''
        possible_states = []
        if len(currentState)==1:
            return []
        for idx in range(len(currentState)-1):
            if currentState[idx] == '+' and currentState[idx+1]=='+':
                possibleString=currentState[:idx]+'--'+currentState[idx+2:]
                possible_states.append(possibleString)
        return possible_states 
        '''   
        