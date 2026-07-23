class Solution:

    def in_bounds(self, neighbor:List[int], grid:List[List[int]]) -> bool:
        return (0 <= neighbor[0] and neighbor[0] < len(grid) 
        and 0 <= neighbor[1] and neighbor[1] < len(grid[0])
        )
    def exploreisland(self, grid:List[List[int]], initial_i:int, initial_j:int) -> int:
        stack = [[initial_i, initial_j]]
        grid[initial_i][initial_j] = 0
        bestvalue = 0
        while(len(stack) > 0):
            current = stack.pop()
            bestvalue+= 1
            #currently directions, subsequently updated the indices
            neighbors = [[-1, 0], [0, -1], [1, 0], [0,1]]
            for neighbor in neighbors:
                neighbor[0] += current[0]
                neighbor[1] += current[1]
                #now they contain the correct grid indices
                if self.in_bounds(neighbor, grid) and grid[neighbor[0]][neighbor[1]] == 1:
                    print(neighbor[0], neighbor[1])
                    stack.append([neighbor[0], neighbor[1]])
                    grid[neighbor[0]][neighbor[1]] = 0
        return bestvalue


            
            

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # another dfs
        # main looks over all cells 
        # explorer function -> modify the grid, update best value
        best = 0
        for i in range (len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j] == 1):
                    best = max(best, self.exploreisland(grid, i, j))
                    print('pinapple')
        return best
            




