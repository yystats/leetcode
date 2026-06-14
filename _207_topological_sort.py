# key idea
# course dependencies: A --> B, A --> C, C --> B, C --> D, B --> D 
# so the course schedule [A, C, B, D]

# assume index
# A = 0, B = 1, C = 2, D = 3
# pre-requisite list = [[1, 0], [2, 0], [1, 2], [3, 2], [3, 1]]

# main idea:
# - get the in-degree for each node (index)
# - get the neighbors of a node (index) points to 

from collections import deque

def topological_sort(num_courses, prerequisite):
    in_degree = [0] * num_courses
    edge = [[] for _ in range(num_courses)]

    for pre in prerequisite:
        edge[pre[1]].append(pre[0])
        in_degree[pre[0]] += 1
    
    queue = deque()
    for i in range(num_courses):
        if in_degree[i] == 0:
            queue.append(i)

    visitedNode = []
    while queue:
        current = queue.popleft()
        visitedNode.append(current)

        for neighbor in edge[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return len(visitedNode) == num_courses


num_courses = 4
prerequisite = [[1, 0], [2, 0], [1, 2], [3, 2], [3, 1]]

print(topological_sort(num_courses, prerequisite))



