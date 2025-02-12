#46. Permutations
#Solved
#Medium
#Topics
#Companies
#Given an array nums of distinct integers, return all the possible 
#permutations
#. You can return the answer in any order.
#
# 
#
#Example 1:
#
#Input: nums = [1,2,3]
#Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#Example 2:
#
#Input: nums = [0,1]
#Output: [[0,1],[1,0]]
#Example 3:
#
#Input: nums = [1]
#Output: [[1]]
# 
#
#Constraints:
#
#1 <= nums.length <= 6
#-10 <= nums[i] <= 10
#All the integers of nums are unique.

class Solution:
    def permuteIterative(self, nums: List[int]) -> List[List[int]]:
        res=[[]]

        for num in nums:
            currRes=[]
            for item in res:
                for i in range(len(item)+1):
                    itemCopy=item[:]
                    itemCopy.insert(i,num)
                    currRes.append(itemCopy)
            res=currRes

        return res    

    def permuteRecursive(self, nums: List[int]) -> List[List[int]]:
        if len(nums)==0:
            return [[]]
        
        res=self.permute(nums[1:])
        num=nums[0]
        currRes=[]
        for item in res:
            
            for i in range(len(item)+1):
                itemCopy=item[:]
                itemCopy.insert(i,num)
                currRes.append(itemCopy)
        res=currRes

        return res
            
