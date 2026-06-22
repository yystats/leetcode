"""
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

"""

def solve(nums: list) -> list[list]:
    # def is_validate_state(state: list, solutions: list[list]) -> bool:
    #     return True if state not in solutions else False

    def get_candidates(state: list, start: int) -> list:
        return range(start, len(nums))

    def search(state: list, start: int, solutions: list[list]) -> None:
        # if is_validate_state(state, solutions):
        solutions.append(state.copy())

        for i in get_candidates(state, start):
            if i > start and nums[i] == nums[i-1]:
                continue
            state.append(nums[i])
            search(state, i + 1, solutions)
            state.pop()
        
    solutions = []
    search([], 0, solutions)

    return solutions

nums = [1,2,2]
print(solve(nums))

