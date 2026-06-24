"""
You are given a 2D binary grid of size m × n, where each cell is either '0'(water) or '1'(land). An island is defined as a group of connected land cells (1s) where connection is only possible through vertical or horizontal neighbors.

For each island in the grid, compute:

- The area: the total number of land cells in the island.
- The number of distinct water cells horizontally or vertically adjacent to the island (the water boundary count). 
A water cell is counted at most once for each island, even if it touches multiple sides of the island. Do not count grid boundaries as water cells.

Return a list of pairs, where each pair contains the area and the water boundary count for an island. The order of the pairs in the output list does not matter.
"""

from collections import deque
from typing import List

def countLandAndWater(grid: List[List[int]]) -> List[List[int]]:
    if not grid or not grid[0]:
        return []

    m, n = len(grid), len(grid[0])
    landVisited = set()
    LAND = 1
    WATER = 0
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    result = []
    for i in range(m):
        for j in range(n):
            if grid[i][j] != LAND or (i,j) in landVisited:
                continue
            
            queue = deque([(i,j)])
            countLand = 0
            waterVisited = set()

            while queue:
                r, c = queue.popleft()
                landVisited.add((r, c))
                countLand += 1
                for dr, dc in direction:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n:
                        if grid[nr][nc] == WATER:
                            waterVisited.add((nr, nc))
                        elif grid[nr][nc] == LAND and (nr, nc) not in landVisited:
                            landVisited.add((nr, nc))
                            queue.append((nr, nc))
            
            result.append([countLand, len(waterVisited)])

    return result

#grid = [[0,1,0],[1,1,0],[0,0,0]]
#grid = [[1,0,1],[0,0,0],[1,0,1]]
grid = [[1,1,1],[1,1,1],[1,1,1]]
print(countLandAndWater(grid))


