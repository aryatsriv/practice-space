# 1838. Frequency of the Most Frequent Element
# Solved
# Medium
# Topics
# Companies
# Hint
# The frequency of an element is the number of times it occurs in an array.

# You are given an integer array nums and an integer k. In one operation, you can choose an index of nums and increment the element at that index by 1.

# Return the maximum possible frequency of an element after performing at most k operations.

 

# Example 1:

# Input: nums = [1,2,4], k = 5
# Output: 3
# Explanation: Increment the first element three times and the second element two times to make nums = [4,4,4].
# 4 has a frequency of 3.
# Example 2:

# Input: nums = [1,4,8,13], k = 5
# Output: 2
# Explanation: There are multiple optimal solutions:
# - Increment the first element three times to make nums = [4,4,8,13]. 4 has a frequency of 2.
# - Increment the second element four times to make nums = [1,8,8,13]. 8 has a frequency of 2.
# - Increment the third element five times to make nums = [1,4,13,13]. 13 has a frequency of 2.
# Example 3:

# Input: nums = [3,9,6], k = 2
# Output: 1
 

# Constraints:

# 1 <= nums.length <= 105
# 1 <= nums[i] <= 105
# 1 <= k <= 105

#Optimal Code:
class Solution:
    def maxFrequencyOptimal(self, nums: List[int], k: int) -> int:
        nums.sort()
        maxFreq=0

        l=0
        r=0
        total=nums[r]
        while r<len(nums):
            if nums[r]*(r-l+1)<=total+k:
                maxFreq=max(r-l+1,maxFreq)
                r+=1
                if r<len(nums):
                    total+=nums[r]
                
            else:
                total-=nums[l]
                l+=1
        
        return maxFreq




# Non optimal solution
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        maxFreq=0

        for i in range(len(nums)-1,-1,-1):
            kLeft=k
            j=i-1
            currFreq=1
            while j>=0 and kLeft>=nums[i]-nums[j]:
                currFreq+=1
                kLeft=kLeft-nums[i]+nums[j]
                j=j-1
            maxFreq=max(currFreq,maxFreq)

        return maxFreq