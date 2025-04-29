#
#Code
#
#
#Testcase
#Testcase
#Test Result
#119. Pascal's Triangle II
#Solved
#Easy
#Topics
#Companies
#Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
#
#In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
#
#
# 
#
#Example 1:
#
#Input: rowIndex = 3
#Output: [1,3,3,1]
#Example 2:
#
#Input: rowIndex = 0
#Output: [1]
#Example 3:
#
#Input: rowIndex = 1
#Output: [1,1]
# 
#
#Constraints:
#
#0 <= rowIndex <= 33
# 
#
#Follow up: Could you optimize your algorithm to use only O(rowIndex) extra space?

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        prev=[]
        for i in range(0,rowIndex+1):
            curr=[1]
            for j in range(1,i+1):
                if j==i:
                    curr.append(1)
                else:
                    curr.append(prev[j-1]+prev[j])
            prev=curr

        return prev

