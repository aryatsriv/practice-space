#64. Minimum Path Sum
#Solved
#Medium
#Topics
#Companies
#Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.
#
#Note: You can only move either down or right at any point in time.
#
# 
#
#Example 1:
#
#
#Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
#Output: 7
#Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
#Example 2:
#
#Input: grid = [[1,2,3],[4,5,6]]
#Output: 12
# 
#
#Constraints:
#
#m == grid.length
#n == grid[i].length
#1 <= m, n <= 200
#0 <= grid[i][j] <= 200

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        cache={}
        def rec(i,j):
            if i>=m or j>=n:
                return sys.maxsize
            if i==m-1 and j==n-1:
                return grid[i][j]
            if (i,j) in cache:
                return cache[(i,j)]

            cache[(i,j)]= grid[i][j]+min(rec(i+1,j),rec(i,j+1)) 
            return cache[(i,j)]
        
        return rec(0,0)
        
    def minPathSumIterative(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])

        next=[0]*n

        for i in range(m-1,-1,-1):
            curr=[0]*n
            for j in range(n-1,-1,-1):
                if j==n-1:
                    curr[j]=next[j]+grid[i][j]
                elif i==m-1:
                    curr[j]=curr[j+1]+grid[i][j]
                else:
                    curr[j]=grid[i][j]+min(curr[j+1],next[j])
            next=curr
            print(next)

        return next[0]

    

            
