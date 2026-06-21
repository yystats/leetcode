# Leetcode 200 

def count_islands(grid: list[list[str]]) -> int:
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    LAND, WATER = "1", "0"

    def sink(r: int, c: int) -> None:
        if not (0 <= r < rows and 0 <= c < cols) or grid[r][c] == WATER:
            return
        grid[r][c] = WATER
        sink(r - 1, c)
        sink(r + 1, c)
        sink(r, c - 1)
        sink(r, c + 1)

    islands = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == LAND:
                islands += 1
                sink(r, c)
    return islands

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(count_islands(grid))
