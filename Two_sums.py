#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

#You may assume that each input would have exactly one solution, and you may not use the same element twice.

#You can return the answer in any order

class Solution:
    def twoSum(self, nums, target):
        # Create a dictionary to store each number and its corresponding index
        num_to_index = {}
        
        # Iterate through the list with indices
        for i, num in enumerate(nums):
            # Calculate the complement for the current number
            complement = target - num
            
            # Check if the complement exists in the dictionary
            if complement in num_to_index:
                # If found, return the indices of the current number and its complement
                return [num_to_index[complement], i]
            
            # Store the current number and its index in the dictionary
            num_to_index[num] = i
        
        # If no solution is found, return an empty list
        return []

# Example usage
nums = [2, 7, 11, 15]
target = 9
solved = Solution()
print(solved.twoSum(nums, target))  # Output: [0, 1] (indices of the numbers 2 and 7)
