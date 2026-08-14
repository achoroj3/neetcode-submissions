class Solution:
    def inbounds(self, row, col, grid):
        return 0 <= row < len(grid) and 0 <= col < len(grid[0])
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        b = []
        nr = len(heights)
        nc = len(heights[0])
        pacific = set()
        atlantic = set()
        for c in range(nc):
            b.append([0, c])
            pacific.add((0,c))
            b.append([nr - 1, c])
            atlantic.add((nr - 1, c))
        for r in range(nr):
            b.append([r, 0])
            pacific.add((r,0))
            b.append([r, nc - 1])
            atlantic.add((r,nc - 1))
        while (len(b) > 0):
            temp = b.pop()
            r, c = temp[0], temp[1]
            directions = [(-1,0),(1,0),(0,-1),(0,1)]
            for dr, dc in directions:
                nr2, nc2 = r + dr, c + dc
                if (self.inbounds(nr2, nc2, heights) and heights[r][c] <= heights[nr2][nc2]) :
                    
                    if (r, c) in pacific and (nr2, nc2) not in pacific:
                        pacific.add((nr2, nc2))
                        b.append([nr2, nc2])
                    if (r, c) in atlantic and (nr2, nc2) not in atlantic:
                        atlantic.add((nr2, nc2))
                        b.append([nr2, nc2])
        return_list = []
        for r in range(nr):
            for c in range(nc):
                if (r,c) in pacific and (r,c) in atlantic:
                    return_list.append([r, c])
        return return_list

        






        
        
            
        


        