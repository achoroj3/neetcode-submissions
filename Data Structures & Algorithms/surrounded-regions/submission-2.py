class Solution:
    def exploreRegion(self, i_cell, board, visited):
        directions = [[-1, 0], [0, -1], [1, 0], [0,1]]
        #check is in bounds and not already seen and is O
        island = [i_cell]
        visited.add(tuple(i_cell))
        while (len(island) > 0):
            cell = island[-1]
            island.pop()
            for dr, dc in directions:
                nr = cell[0] + dr
                nc = cell[1] + dc
                if (0 <= nr < len(board) and 0 <= nc < len(board[0])
                and (tuple([nr, nc]) not in visited) and board[nr][nc] == 'O'):
                    island.append([nr, nc])
                    visited.add(tuple([nr, nc]))
        

    def solve(self, board: List[List[str]]) -> None:
        # get border elements
        # if O on border, then take adjacent island and put into "not surrounded"
        #modify graph based on not surrounded list
        b = []
        nr = len(board)
        nc = len(board[0])
        visited = set()
        for c in range(nc):
            b.append([0, c])
            b.append([nr - 1, c])
        for r in range(1, nr - 1):
            b.append([r, 0])
            b.append([r, nc - 1])
        while(len(b) > 0):
            cell = b[-1]
            b.pop()
            if board[cell[0]][cell[1]] == 'O' and tuple(cell) not in visited:
                self.exploreRegion(cell, board, visited)
        for r in range(nr):
            for c in range(nc):
                #surrounded
                if (tuple([r, c]) not in visited):
                    board[r][c] = 'X'
#fingers crossed

            

