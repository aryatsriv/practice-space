#16. 3Sum Closest
#Solved
#Medium
#Topics
#Companies
#Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.
#
#Return the sum of the three integers.
#
#You may assume that each input would have exactly one solution.
#
# 
#
#Example 1:
#
#Input: nums = [-1,2,1,-4], target = 1
#Output: 2
#Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
#Example 2:
#
#Input: nums = [0,0,0], target = 1
#Output: 0
#Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
# 
#
#Constraints:
#
#3 <= nums.length <= 500
#-1000 <= nums[i] <= 1000
#-104 <= target <= 104
#
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closestSum=nums[0]+nums[1]+nums[2]
        for i in range(len(nums)-1):
            j=i+1
            k=len(nums)-1

            while j<k:
                if nums[i]+nums[j]+nums[k]==target:
                    return target    
                else:
                    currSum=nums[i]+nums[j]+nums[k]
                    if (abs(currSum-target)<abs(closestSum-target)):
                        closestSum=currSum
                    if nums[i]+nums[j]+nums[k]>target: 
                        k=k-1
                    else:
                        j=j+1

        return closestSum
        
