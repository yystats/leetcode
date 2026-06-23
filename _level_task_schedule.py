"""
A company is asked to efficiently schedule a set of tasks, each identified by a unique, non-empty lowercase string. 
Tasks have dependencies: each dependency is a pair [fromTask, toTask], meaning fromTask must finish before toTask can begin.

The company has unlimited machines available, so at any given time, all tasks that are ready (no unmet dependencies) can be run in parallel. 
Your job is to determine the schedule by grouping tasks that can be executed together at each time step. The schedule should be a list of groups, 
where:

- Each group contains all tasks that start at the same time.
- The order of groups reflects the overall execution order (earlier groups must finish before later groups can begin).
- Within each group, tasks must be ordered in lexicographic order.
- Return an empty list if it's not possible to finish all tasks.

Input: dependencies = [["a", "b"], ["c", "d"], ["e", "f"]]
Output: [["a", "c", "e"], ["b", "d", "f"]]
"""

# idea 
# 1. build graph 
# 2. build indegree  
# 3. process level by level 
# 4. final check if there is a cyclic task 

from collections import defaultdict, deque

def getLevelTaskSchedule(dependencies: list[list]) -> list[list]:
    # build graph
    graph = defaultdict(list)
    inDegree = {}
    allTasks = set()

    for from_task, to_task in dependencies:
        graph[from_task].append(to_task)

        if from_task not in inDegree:
            inDegree[from_task] = 0
        if to_task not in inDegree:
            inDegree[to_task] = 0
        
        if to_task in inDegree:
            inDegree[to_task] += 1

        allTasks.add(from_task)
        allTasks.add(to_task)

    queue = deque()
    for task, degree in inDegree.items():
        if degree == 0:
            queue.append(task)

    results = []
    processedCount = 0
    while queue:
        levelSize = len(queue)
        currentLevel = []

        for i in range(levelSize):
            current_task = queue.popleft()
            processedCount += 1
            currentLevel.append(current_task)

            # process neighbors
            neighbors = graph[current_task]
            if neighbors:
                for neighbor in neighbors:
                    inDegree[neighbor] -= 1

                    if inDegree[neighbor] == 0:
                        queue.append(neighbor)
        
        currentLevel.sort()
        results.append(currentLevel)

    if processedCount != len(allTasks):
        return []

    return results

    # print(inDegree)
    # print(graph)
    # print(allTasks)

#dependencies = [["a", "b"], ["c", "d"], ["e", "f"], ["g", "b"]]
dependencies = [["a", "b"], ["c", "d"], ["e", "f"]]

print(getLevelTaskSchedule(dependencies))

