# 34. Find First and Last Position of Element in Sorted Array
# Solved
# Medium
# Topics
# Companies
# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:

# Input: nums = [], target = 0
# Output: [-1,-1]
 

# Constraints:

# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109
# nums is a non-decreasing array.
# -109 <= target <= 109
class Solution:
    def startIndex(self,arr,target):
        s=0
        e=len(arr)-1
        floor=-1
        while s<=e:
            mid=(s+e)//2
            if arr[mid]==target:
                floor=mid
                e=mid-1
            elif arr[mid]>target:
                e=mid-1
            else: 
                s=mid+1

        return floor

    def endIndex(self,arr,target):
        s=0
        e=len(arr)-1
        ceil=-1
        while s<=e:
            mid=(s+e)//2
            if arr[mid]==target:
                ceil=mid
                s=mid+1
            elif arr[mid]>target:
                e=mid-1
            else: 
                s=mid+1

        return ceil
            
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.startIndex(nums,target),self.endIndex(nums,target)]
        