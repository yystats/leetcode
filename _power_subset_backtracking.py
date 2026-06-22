"""
Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
"""

# backtracking to solve the problem 
# state = [], [1]

def is_valid_state(state: list) -> bool:
    return True

def get_candidates(nums: list, state: list, start: int) -> list:
    return range(start, len(nums))
    
def search(nums: list, state: list, start: int, solutions: list[list]) -> None:
    if is_valid_state(state):
        solutions.append(state.copy())
    
    for i in get_candidates(nums, state, start):
        state.append(nums[i])
        search(nums, state, i + 1, solutions)
        state.pop()

def solve(nums) -> list[list]:
    solutions = []
    search(nums, [], 0, solutions)
    return solutions

nums = [1,2,3]
print(solve(nums))


