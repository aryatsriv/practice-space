#
#74. Search a 2D Matrix
#Solved
#Medium
#Topics
#Companies
#You are given an m x n integer matrix matrix with the following two properties:
#
#Each row is sorted in non-decreasing order.
#The first integer of each row is greater than the last integer of the previous row.
#Given an integer target, return true if target is in matrix or false otherwise.
#
#You must write a solution in O(log(m * n)) time complexity.
#
# 
#
#Example 1:
#
#
#Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
#Output: true
#Example 2:
#
#
#Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
#Output: false
# 
#
#Constraints:
#
#m == matrix.length
#n == matrix[i].length
#1 <= m, n <= 100
#-104 <= matrix[i][j], target <= 104

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rs=0
        re=len(matrix)-1
        cs=0
        ce=len(matrix[0])-1

        while rs<=re:
            mid=(rs+re)//2
            if matrix[mid][ce]>=target and matrix[mid][cs]<=target:
                break
            elif matrix[mid][ce]<target:
                rs=mid+1
            else:
                re=mid-1

        if rs>re:
            return False
        
        row=(rs+re)//2

        while cs<=ce:
            mid=(cs+ce)//2
            if matrix[row][mid]==target:
                return True
            elif matrix[row][mid]>target:
                ce=mid-1
            else:
                cs=mid+1
        
        return False
        
