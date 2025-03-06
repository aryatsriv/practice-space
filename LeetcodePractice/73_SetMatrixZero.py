#73. Set Matrix Zeroes
#Solved
#Medium
#Topics
#Companies
#Hint
#Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
#
#You must do it in place.
#
# 
#
#Example 1:
#
#
#Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
#Output: [[1,0,1],[0,0,0],[1,0,1]]
#Example 2:
#
#
#Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
#Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
# 
#
#Constraints:
#
#m == matrix.length
#n == matrix[0].length
#1 <= m, n <= 200
#-231 <= matrix[i][j] <= 231 - 1
# 
#
#Follow up:
#
#A straightforward solution using O(mn) space is probably a bad idea.
#A simple improvement uses O(m + n) space, but still not the best solution.
#Could you devise a constant space solution?


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rowZero=False
        m,n=len(matrix),len(matrix[0])
        
        for i in range(m):
            for j in range(n):
                if i==0:
                    if matrix[i][j]==0:
                        rowZero=True
                else:
                    if matrix[i][j]==0:
                        matrix[i][0]=0
                        matrix[0][j]=0
        

        for i in range(m-1,0,-1):
            for j in range(n-1,-1,-1):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0
        

        if rowZero:
            for j in range(n):
                matrix[0][j]=0


