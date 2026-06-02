class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = len(board)
        col = len(board[0])
        for i in range(row):
            temp= []
            for j in range(col):
                if(board[i][j]!= "."):
                    if(board[i][j] in temp):
                        return False
                    temp.append(board[i][j])
        for j in range(col):
            temp= []
            for i in range(row):
                if(board[i][j]!= "."):
                    if(board[i][j] in temp):
                        return False
                    temp.append(board[i][j])
        for row in range(0,9,3):
             for col in range(0,9,3):
                temp=[]
                for i in range(3):
                    for j in range(3):
                        val = board[row + i][col + j]

                        if val != ".":

                            if val in temp:
                                return False

                            temp.append(val)

    
        return True