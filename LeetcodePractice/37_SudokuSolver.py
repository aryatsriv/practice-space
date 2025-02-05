# 37. Sudoku Solver
# Hard
# Topics
# Companies
# Write a program to solve a Sudoku puzzle by filling the empty cells.

# A sudoku solution must satisfy all of the following rules:

# Each of the digits 1-9 must occur exactly once in each row.
# Each of the digits 1-9 must occur exactly once in each column.
# Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
# The '.' character indicates empty cells.

 

# Example 1:


# Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
# Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
# Explanation: The input board is shown above and the only valid solution is shown below:


 

# Constraints:

# board.length == 9
# board[i].length == 9
# board[i][j] is a digit or '.'.
# It is guaranteed that the input board has only one solution.
class Solution:
    def isValid(self,board,r,c):
            for i in range(9):
                if i!=c and board[r][i]==board[r][c]:
                    return False
                if i!=r and board[i][c]==board[r][c]:
                    return False
            
            boxS=(r//3)*3
            boxC=(c//3)*3
            for i in range(boxS,boxS+3):
                for j in range(boxC,boxC+3):
                    if i!=r and j!=c and board[i][j]==board[r][c]:

                        return False
            return True
    
    def solveSudoku(self, board: List[List[str]]) -> None:  
        def rec(i,j):
            if i>=9:
                return True
            if j>=9:
                return rec(i+1,0)

            if board[i][j]=='.':       
                for val in range(1,10):
                    board[i][j]=str(val)
                    if self.isValid(board,i,j) and rec(i,j+1):
                        return True
                board[i][j]='.'
                return False
                


            else:
                if self.isValid(board,i,j):
                    return rec(i,j+1)
                else:
                    return False
            return False
        
        rec(0,0)

        return board
