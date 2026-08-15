from collections import deque
class Solution:

    def traversable(self, nr, nc, grid) -> bool:
        #check in bounds and its empty or is improvement
        return 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 2147483647
        
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # find all treasure chests
        # from treasure chests, bfs outwards
        # DO NOT TRAVERSE TO -1, do NOT traverse to non INF, or 0.
        
        chests = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (grid[i][j] == 0):
                    chests.append([i, j])
        distance = 0
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        route = deque(chests)
        while (len(route) > 0):
            level_size = len(route)
            while(level_size > 0): #level = distance to chest
                node = route.popleft()
                for dr, dc in directions:
                    if self.traversable(node[0] + dr,node[1] + dc, grid):
                        grid[node[0] + dr][node[1] + dc] = distance + 1
                        route.append([node[0] + dr,node[1] + dc])
                level_size-= 1
            distance+= 1
                

                


