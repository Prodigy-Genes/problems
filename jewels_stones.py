#You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

#Letters are case sensitive, so "a" is considered a different type of stone from "A".



class Solution:
    def numJewelsinStones(self, jewels, stones):
        sum = 0
        for stone in stones:
            if stone in jewels:
                sum+=1
        return sum
            

jewels = "aA"
stones = "aAAbbbb"
solved = Solution()
print(f"{solved.numJewelsinStones(jewels, stones)}")
