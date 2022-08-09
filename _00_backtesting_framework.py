"""
backtesting introduction
reference: 
- https://www.youtube.com/watch?v=A80YzvNwqXA
- https://gist.github.com/RuolinZheng08/cdd880ee748e27ed28e0be3916f56fa6
- understand backtracking pop: https://stackoverflow.com/questions/67355764/why-do-we-pop-from-the-list-at-the-end-of-each-backtrack-iteration
"""

"""
Template 
"""
def is_valida_state(state):
    # check if it is a validd solution
    return True 

def get_candidates(state):
    return []

def search(state, solutions):
    if is_valida_state(state):
        solutions.append(state.copy())
        # if we just need one solution, we can return immediately
        # return      

    for candidate in get_candidates(state):
        state.add(candidate) 
        search(state, solutions)
        state.remove(candidate)

def solve():
    solutions = []
    state = set()
    search(state, solutions)
    return solutions 


