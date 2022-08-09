"""
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target.
You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

"""
class solveCombinationSum:
    def isValidState(self, state, target):
        return sum(state) == target
    
    def getCandidates(self, state, nums, target):
        if not state: 
            return nums
        
        candidates = []
        index = nums.index(state[-1])
        
        for i in range(index, len(nums)):
            if nums[i] + sum(state) <= target:
                candidates.append(nums[i])
                
        return candidates
                
    
    def search(self, state, nums, target, solutions):
        if self.isValidState(state, target) and state not in solutions:
            solutions.append(state.copy())

        for candidate in self.getCandidates(state, nums, target):
            state.append(candidate)
            self.search(state, nums, target, solutions)
            state.pop()
    
    def solve(self, nums, target):
        solutions = []
        state = []
        self.search(state, nums, target, solutions)
        
        return solutions

nums = [2,3,5]
target = 8
res = solveCombinationSum()
print(res.solve(nums, target))
