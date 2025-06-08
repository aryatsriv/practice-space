#198. House Robber
#Solved
#Medium
#Topics
#Companies
#You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
#
#Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
#
# 
#
#Example 1:
#
#Input: nums = [1,2,3,1]
#Output: 4
#Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
#Total amount you can rob = 1 + 3 = 4.
#Example 2:
#
#Input: nums = [2,7,9,3,1]
#Output: 12
#Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
#Total amount you can rob = 2 + 9 + 1 = 12.
# 
#
#Constraints:
#
#1 <= nums.length <= 100
#0 <= nums[i] <= 400

class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        cache={}
        def rec(i):
            if i>=n:
                return 0
            if i in cache:
                return cache[i]
            val1=nums[i]+rec(i+2)
            val2=rec(i+1)
            cache[i]= max(val1,val2)
            return cache[i]


        return rec(0)


    def rob_iterative(self, nums: List[int]) -> int:
        n=len(nums)
        cache=[0]*n

        for i in range(n):
            num=nums[i]
            val1=0 if i-1<0 else cache[i-1]
            val2=num if i-2<0 else cache[i-2]+num
            cache[i]=max(val1,val2)


        return cache[n-1]
