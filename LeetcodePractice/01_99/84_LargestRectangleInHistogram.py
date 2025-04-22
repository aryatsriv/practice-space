#84. Largest Rectangle in Histogram
#Solved
#Hard
#Topics
#Companies
#Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.
#
# 
#
#Example 1:
#
#
#Input: heights = [2,1,5,6,2,3]
#Output: 10
#Explanation: The above is a histogram where width of each bar is 1.
#The largest rectangle is shown in the red area, which has an area = 10 units.
#Example 2:
#
#
#Input: heights = [2,4]
#Output: 4
# 
#
#Constraints:
#
#1 <= heights.length <= 105
#0 <= heights[i] <= 104

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
