#59. Spiral Matrix II
#Solved
#Medium
#Topics
#Companies
#Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.
#
# 
#
#Example 1:
#
#
#Input: n = 3
#Output: [[1,2,3],[8,9,4],[7,6,5]]
#Example 2:
#
#Input: n = 1
#Output: [[1]]
# 
#
#Constraints:
#
#1 <= n <= 20
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        matrix=[[0 for i in range(n)] for j in range(n)]
        l,r,t,b=0,n-1,0,n-1
        count=1
        while l<=r and t<=b:
            for i in range(l,r+1):
                matrix[t][i]=count
                count+=1
            t+=1
            
            for i in range(t,b+1):
                matrix[i][r]=count
                count+=1
            r-=1

            if t<=b:
                for i in range(r,l-1,-1):
                    matrix[b][i]=count
                    count+=1
                b-=1

            if l<=r:
                for i in range(b,t-1,-1):
                    matrix[i][l]=count
                    count+=1
                l+=1

        return matrix
