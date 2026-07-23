class Solution:
    def in_bounds(self, row:int , col:int, max_row:int, max_col:int) -> bool:
        return row < max_row and row >= 0 and col < max_col and col >= 0
    def discover_island(self, grid: List[List[str]], init_row: int, init_col: int):
        visited = [[init_row, init_col]]
        while len(visited) > 0:
            row = visited[-1][0]
            col = visited[-1][1]
            visited.pop(-1)
            if (grid[row][col] == "1"):
                grid[row][col] = "0"
                neighbors = [[row - 1, col], [row, col - 1],
                [row, col + 1],[row + 1, col]]
                for neighbor in neighbors:
                    n_row = neighbor[0]
                    n_col = neighbor[1]
                    if (self.in_bounds(n_row, n_col, len(grid), len(grid[0])) 
                    and grid[n_row][n_col] == "1"):
                        visited.append(neighbor.copy())
            
    def numIslands(self, grid: List[List[str]]) -> int:
        #convert grid to a graph?
        #then traverse graph
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.discover_island(grid, i, j)
                    count += 1
        return count
        
