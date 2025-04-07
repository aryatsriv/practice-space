#90. Subsets II
#Solved
#Medium
#Topics
#Companies
#Given an integer array nums that may contain duplicates, return all possible subsets (the power set).
#
#The solution set must not contain duplicate subsets. Return the solution in any order.
#
# 
#
#Example 1:
#
#Input: nums = [1,2,2]
#Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
#Example 2:
#
#Input: nums = [0]
#Output: [[],[0]]
# 
#
#Constraints:
#
#1 <= nums.length <= 10
#-10 <= nums[i] <= 10

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        curr=[]
        n=len(nums)
        def rec(i):
            if i==n:
                res.append(curr[:]) 
                return
            curr.append(nums[i])
            rec(i+1)
            curr.pop()
            j=i+1
            #what this is essentialy doing is eliminating the possibility of haveing same value at same index in the "curr" variable which is a list
            while j<n and nums[j]==nums[i]:
                j+=1
            rec(j)

        rec(0)

        return res
