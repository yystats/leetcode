
def maxIslandPerimeter(grid: list[list[str]]) -> int:
    if not grid or not grid[0]:
        return 0
        
    m, n = len(grid), len(grid[0])
    visited = set()
    max_perimeter = 0
    LAND, WATER = 1, 0
    
    def dfs(r: int, c: int) -> int:
        # If out of bounds or water, this edge contributes 1 to the perimeter
        if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == WATER:
            return 1
        
        # If already visited land, it contributes 0 to the perimeter 
        # (as it was handled or will be handled by another recursive step)
        if (r, c) in visited:
            return 0
            
        # Mark the current land cell as visited
        visited.add((r, c))
        
        # Explore all 4 directions and sum up their perimeter contributions
        perimeter = 0
        perimeter += dfs(r + 1, c) # Down
        perimeter += dfs(r - 1, c) # Up
        perimeter += dfs(r, c + 1) # Right
        perimeter += dfs(r, c - 1) # Left
        
        return perimeter

    # Traverse the entire grid to find all islands
    for r in range(m):
        for c in range(n):
            if grid[r][c] == LAND and (r, c) not in visited:
                # Calculate the perimeter of the newly found island
                current_perimeter = dfs(r, c)
                max_perimeter = max(max_perimeter, current_perimeter)
                
    return max_perimeter

grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
print(maxIslandPerimeter(grid))

