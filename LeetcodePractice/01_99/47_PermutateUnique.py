#47. Permutations II
#Solved
#Medium
#Topics
#Companies
#Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.
#
# 
#
#Example 1:
#
#Input: nums = [1,1,2]
#Output:
#[[1,1,2],
# [1,2,1],
# [2,1,1]]
#Example 2:
#
#Input: nums = [1,2,3]
#Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# 
#
#Constraints:
#
#1 <= nums.length <= 8
#-10 <= nums[i] <= 10
#
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res=[[]]

        for num in nums:
            currRes=[]
            cache=set()
            for item in res:
                for i in range(len(item)+1):
                    itemCopy=item[:]
                    itemCopy.insert(i,num)
                    if tuple(itemCopy) not in cache:
                        cache.add(tuple(itemCopy))
                        currRes.append(itemCopy)
            res=currRes

        return res    
