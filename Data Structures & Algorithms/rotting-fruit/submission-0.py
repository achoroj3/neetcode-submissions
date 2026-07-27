class Solution:
    def in_bounds(self, neighbor:List[int], grid: List[List[int]]) -> bool:
        return neighbor[0] < len(grid) and 0 <= neighbor[0] and neighbor[1] < len(grid[0]) and 0 <= neighbor[1]

    def orangesRotting(self, grid: List[List[int]]) -> int:
        #make a list of the rotting oranges
        #then on every iteration, make surrounding oranges rot if they exist
        
        rotten = []
        num_fresh = 0
        num_minutes = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    rotten.append([i, j])
                if grid[i][j] == 1:
                    num_fresh+=1
        while (num_fresh > 0):
            current_minute_rotten = rotten.copy()
            rotting_stopped = True
            for elem in current_minute_rotten:
                neighbors = [[-1, 0], [1, 0], [0, -1], [0, 1]]
                for neighbor in neighbors:
                    neighbor[0] += elem[0]
                    neighbor[1] += elem[1]
                    if self.in_bounds(neighbor, grid) and grid[neighbor[0]][neighbor[1]] == 1:
                        rotten.append([neighbor[0],neighbor[1]])
                        grid[neighbor[0]][neighbor[1]] = 2
                        num_fresh-= 1
                        rotting_stopped = False
            if rotting_stopped:
                return -1
            num_minutes+=1
        return num_minutes
                        
        