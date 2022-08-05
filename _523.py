"""
Continuous Subarray Sum

Given an integer array nums and an integer k, return true if nums has a continuous subarray of size at least two whose elements sum up to a multiple of k, or false otherwise.
An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.

Input: nums = [23,2,4,6,7], k = 6
Output: true
Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.
"""

def checkSubarraySum(nums, k):
    """
    key ideas:
    - use cumsum
    - cumsum_i % k == cumsum_j % k then the difference between i, j = n*k; e.g.k = 2, at i = 1, cusum = 3, res = 1; at j = 5, cumsum = 11, res = 1
    - we only need to store the first index of res if there are multiple same res
    - dict[0] = -1 is bit tricky that handles the case, e.g. nums = [2, 2]; k = 4 --> i = 1 and i - dict[0] = 2
    """
    import collections

    cumsum = 0
    dict = collections.defaultdict(int)
    dict[0] = -1

    for i in range(len(nums)):
        cumsum += nums[i]
        res = cumsum % k 

        if res in dict and i - dict[res] >= 2:
            return True 
        
        if res not in dict:
            dict[res] = i

    return False 


nums = [23,2,4,6,7]
k = 6
print(checkSubarraySum(nums, k))

