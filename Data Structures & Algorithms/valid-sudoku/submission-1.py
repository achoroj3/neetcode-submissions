class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
      #check rows
        for i in range(9):
            unique = set()
            for j in range(9):
                if board[i][j] in unique:
                    
                    return False
                if board[i][j] != "." :
                    unique.add(board[i][j])

        for i in range(9):
            unique = set()
            for j in range(9):
                if board[j][i] in unique:
                    return False
                if board[j][i] != "." :
                    unique.add(board[j][i])
        #this is the hard part
        adict = {
            (0, 0): set(),
            (0, 1): set(),
            (0, 2): set(),
            (1, 0): set(),
            (1, 1): set(),
            (1, 2): set(),
            (2, 0): set(),
            (2, 1): set(),
            (2, 2): set()
        }
        for i in range(9):
            for j in range(9):
                if board[i][j] in adict[(i//3, j//3)]:
                    return False
                if board[i][j] != ".":
                    adict[(i//3, j//3)].add(board[i][j])
            
            

        return True

        