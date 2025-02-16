#52. N-Queens II
#Hard
#Topics
#Companies
#The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
#
#Given an integer n, return the number of distinct solutions to the n-queens puzzle.
#
# 
#
#Example 1:
#
#
#Input: n = 4
#Output: 2
#Explanation: There are two distinct solutions to the 4-queens puzzle as shown.
#Example 2:
#
#Input: n = 1
#Output: 1
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

    def totalNQueens(self, n: int) -> int:
        curr=[['.' for _ in range(n)] for _ in range(n)]
        count=0
        def rec(i):
            if i>=n:
                nonlocal count
                count+=1
            for j in range(0,n):
                if self.isValid(curr,i,j,n):
                    curr[i][j]='Q'
                    rec(i+1)
                    curr[i][j]='.'
                    
            return

        rec(0)

        return count
        
