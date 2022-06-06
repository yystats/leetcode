def twoSums(nums, target):
    """
    nums: a list
    target: an int 
    """

    dict = {}

    for i in range(len(nums)):
        if target - nums[i] in dict:
            return [dict[target - nums[i]], i]
        else:
            dict[nums[i]] = i

## Run Test 
import unittest 

class TestStringMethods(unittest.TestCase):
    def test(self):
        res = twoSums(nums=[2,7,11,15], target=9)
        self.assertTrue(res==[0,1] or res==[1,0]) 


if __name__ == '__main__':
    unittest.main()

