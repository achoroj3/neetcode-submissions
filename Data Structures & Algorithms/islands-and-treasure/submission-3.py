from collections import deque
class Solution:

    def traversable(self, nr, nc, grid) -> bool:
        #check in bounds and its empty or is improvement
        return 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 2147483647

    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        chests = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (grid[i][j] == 0):
                    chests.append([i, j])
        distance = 0
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        route = deque(chests)
        while (len(route) > 0):
                node = route.popleft()
                for dr, dc in directions:
                    if self.traversable(node[0] + dr,node[1] + dc, grid):
                        grid[node[0] + dr][node[1] + dc] = grid[node[0]][node[1]] + 1
                        route.append([node[0] + dr,node[1] + dc])
# do not process node by node, process in layers from node collection
# you can use the current value to calculate the next level's value for distance
        

                


