"""
You are given an integer array nums. You are initially positioned at the array's first index, 
and each element in the array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.
"""

# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

"""
idea: it is a bit tricky that we wanna compare the index with max jump.  
"""

def canJump(nums):
    if len(nums) == 0:
        return False 
    
    max_jump = nums[0]
    for i in range(1, len(nums)):
        if i > max_jump:
            return False 
        max_jump = max(max_jump, nums[i]+i)

    return True 

nums = [2,3,1,1,4]
print(canJump(nums))

