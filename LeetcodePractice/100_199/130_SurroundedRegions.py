#130. Surrounded Regions
#Solved
#Medium
#Topics
#Companies
#You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:
#
#Connect: A cell is connected to adjacent cells horizontally or vertically.
#Region: To form a region connect every 'O' cell.
#Surround: The region is surrounded with 'X' cells if you can connect the region with 'X' cells and none of the region cells are on the edge of the board.
#To capture a surrounded region, replace all 'O's with 'X's in-place within the original board. You do not need to return anything.
#
# 
#
#Example 1:
#
#Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
#
#Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
#
#Explanation:
#
#
#In the above diagram, the bottom region is not captured because it is on the edge of the board and cannot be surrounded.
#
#Example 2:
#
#Input: board = [["X"]]
#
#Output: [["X"]]
#
# 
#
#Constraints:
#
#m == board.length
#n == board[i].length
#1 <= m, n <= 200
#board[i][j] is 'X' or 'O'.

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        q=deque()
        m=len(board)
        n=len(board[0])
        for i in range(m):
            if board[i][0]=='O':
                q.append((i,0))
            if board[i][n-1]=='O':
                q.append((i,n-1))
        
        for i in range(n):
            if board[0][i]=='O':
                q.append((0,i))
            if board[m-1][i]=='O':
                q.append((m-1,i))

        ri=[-1,0,0,1]
        ci=[0,-1,1,0]
        while q:
            r,c=q.popleft()
            board[r][c]='A'
            for i in range(4):
                nr=r+ri[i]
                nc=c+ci[i]
                if nr>=0 and nr<m and nc>=0 and nc<n:
                    if board[nr][nc]=='O':
                        q.append((nr,nc))
        
        for i in range(m):
            for j in range(n):
                if board[i][j]=='O':
                    board[i][j]='X'
                if board[i][j]=='A':
                    board[i][j]='O'
        
