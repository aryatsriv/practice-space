#85. Maximal Rectangle
#Solved
#Hard
#Topics
#Companies
#Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.
#
# 
#
#Example 1:
#
#
#Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
#Output: 6
#Explanation: The maximal rectangle is shown in the above picture.
#Example 2:
#
#Input: matrix = [["0"]]
#Output: 0
#Example 3:
#
#Input: matrix = [["1"]]
#Output: 1
# 
#
#Constraints:
#
#rows == matrix.length
#cols == matrix[i].length
#1 <= row, cols <= 200
#matrix[i][j] is '0' or '1'.
#
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st=[]
        i=0
        maxArea=0
        while i<len(heights):
            height=heights[i]
            start=i
            while st and st[-1][1]>height:
                maxArea=max(st[-1][1]*(i-st[-1][0]),maxArea)
                start=st[-1][0]
                st.pop()
            st.append([start,height])
            i+=1
        
        while st:
            maxArea=max(st[-1][1]*(len(heights)-st[-1][0]),maxArea)
            st.pop()

        return maxArea

        
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m,n=len(matrix),len(matrix[0])
        maxArea=0
        heights=[0]*n
        for i in range(m):
            for j in range(n):
                if matrix[i][j]=='0':
                    heights[j]=0
                else:
                    heights[j]=heights[j]+int(matrix[i][j])
            maxArea=max(maxArea,self.largestRectangleArea(heights))

        return maxArea
