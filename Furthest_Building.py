#You are given an integer array heights representing the heights of buildings, some bricks, and some ladders.

#You start your journey from building 0 and move to the next building by possibly using bricks or ladders.

#While moving from building i to building i+1 (0-indexed),

#If the current building's height is greater than or equal to the next building's height, you do not need a ladder or bricks.
#If the current building's height is less than the next building's height, you can either use one ladder or (h[i+1] - h[i]) bricks.
#Return the furthest building index (0-indexed) you can reach if you use the given ladders and bricks optimally.

import heapq

class Solution:
    def furthestBuilding(self, heights, bricks, ladders):
        used_bricks = []  # Keep track of used bricks
        
        for i in range(len(heights) - 1):
            diff = heights[i + 1] - heights[i]
            
            if diff <= 0:  # No need for bricks or ladders
                continue
            else:
                heapq.heappush(used_bricks, diff)  # Store the difference in the heap
                if len(used_bricks) > ladders:  # If more ladders are needed, use bricks
                    bricks -= heapq.heappop(used_bricks)
                    if bricks < 0:  # If bricks are insufficient, return the current index
                        return i
        return len(heights) - 1

# Example usage
heights1 = [4, 2, 7, 6, 9, 14, 12]
bricks1 = 5
ladders1 = 1
heights2 = [4, 12, 2, 7, 3, 18, 20, 3, 19]
bricks2 = 10
ladders2 = 2
heights3 = [14, 3, 19, 3]
bricks3 = 17
ladders3 = 0
heights4 = [1, 5, 1, 2, 3, 4, 10000]
bricks4 = 4
ladders4 = 1

solved = Solution()
print(solved.furthestBuilding(heights1, bricks1, ladders1))  # Output: 4
print(solved.furthestBuilding(heights2, bricks2, ladders2))  # Output: 7
print(solved.furthestBuilding(heights3, bricks3, ladders3))  # Output: 3
print(solved.furthestBuilding(heights4, bricks4, ladders4))  # Output: 5
