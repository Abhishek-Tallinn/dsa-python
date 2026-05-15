# Problem: Leetcode 2069 - Walking Robot Simulation II
# Difficulty: Medium
# Link: https://leetcode.com/problems/walking-robot-simulation-ii/description/
# Time Complexity: O(w+h) as now we used modulo operator
# Space Complexity: O(1) as only direction vectors and x and y values stored
# Approach: It is important to note that robot moves in a fixed cycling path which repeats and hence we can reduce the operations with modulus operator.
# as simulating all operations leads to TLE. we can calculate perimeters and see how many round the robot will do and then only calculate the position change for the current round.


class Robot:

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.x = self.y = 0
        self.d_vectors = [(1,0),(0,1),(-1,0),(0,-1)]
        self.dir_index = 0
        
    def step(self, num: int) -> None:
        dx,dy = self.d_vectors[self.dir_index]
        perimeter = 2*(self.width-1+self.height-1)
        num = num%perimeter
        if num==0:
            if self.x==0 and self.y==0:
                self.dir_index = 3
        while num > 0:
            if (self.x+dx >= self.width):
                self.dir_index = (self.dir_index+1)%4
                dx,dy = self.d_vectors[self.dir_index]
            elif (self.y+dy >= self.height):
                self.dir_index = (self.dir_index+1)%4
                dx,dy = self.d_vectors[self.dir_index]
            elif dx==-1 and self.x-abs(dx)<0:
                self.dir_index = (self.dir_index+1)%4
                dx,dy = self.d_vectors[self.dir_index]
            elif dy==-1 and self.y-abs(dy)<0:
                self.dir_index = (self.dir_index+1)%4
                dx,dy = self.d_vectors[self.dir_index]
            self.x+=dx
            self.y+=dy
            num-=1

    def getPos(self) -> List[int]:
        return [self.x,self.y]
        
    def getDir(self) -> str:
        if self.dir_index==0: return "East"
        elif self.dir_index==1: return "North"
        elif self.dir_index==2: return "West"
        else: 
            return "South" 

# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()