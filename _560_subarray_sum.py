"""
Subarray Sum Equals K

Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
A subarray is a contiguous non-empty sequence of elements within an array.

Input: nums = [1,2,3], k = 3
Output: 2
"""

def subArraySum(nums, k):
    """
    key: 
    - use the cummulative sum 
    - use dictionary to save the cumsum as dict[cumsum] += 1; here we need to save the number of same cumsum as they could appear at different index 
    """

    import collections

    count, cumsum = 0, 0
    dict = collections.defaultdict(int)
    dict[0] = 1  # must have dict[0]

    for i in range(len(nums)):
        cumsum += nums[i]

        if cumsum - k in dict:
            count += dict[cumsum - k]

        dict[cumsum] += 1

    return count 

# test case 
nums = [1,2,3]
k = 3

print(subArraySum(nums, k))



