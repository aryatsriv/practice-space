#51. N-Queens
#Solved
#Hard
#Topics
#Companies
#The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
#
#Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.
#
#Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.
#
# 
#
#Example 1:
#
#
#Input: n = 4
#Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
#Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
#Example 2:
#
#Input: n = 1
#Output: [["Q"]]
# 
#
#Constraints:
#
#1 <= n <= 9
class Solution:
    def isValid(self,l,r,c,n):
        for i in range(0,r):
            if l[i][c]=='Q':
                return False
        for i in range(0,c):
            if l[r][i]=='Q':
                return False
        for i in range(r-1,-1,-1):
            j=c-(r-i)
            if j>=0 and l[i][j]=='Q':
                return False 
            j=c+(r-i)
            if j<n and l[i][j]=='Q':
                return False
        return True

    def solveNQueens(self, n: int) -> List[List[str]]:
        curr=[['.' for _ in range(n)] for _ in range(n)]
        res=[]
        def rec(i):
            if i>=n:
                joinedCurr=["".join(ele) for ele in curr]
                res.append(joinedCurr)

            for j in range(0,n):
                if self.isValid(curr,i,j,n):
                    curr[i][j]='Q'
                    rec(i+1)
                    curr[i][j]='.'

            return

        rec(0)

        return res
