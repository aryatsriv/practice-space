# 4. Median of Two Sorted Arrays
# Solved
# Hard
# Topics
# Companies
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

 

# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# Example 2:

# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

# Constraints:

# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -106 <= nums1[i], nums2[i] <= 106

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums2)>len(nums1):
            return self.findMedianSortedArrays(nums2,nums1)

        m,n=len(nums1),len(nums2)
        midLen=(m+n)//2
        s=0
        e=n-1

        while True:
            i=(s+e)//2
            j=midLen-i-2
            l2Max=-sys.maxsize-1 if i<0 else nums2[i]
            l1Max=-sys.maxsize-1 if j<0 else nums1[j]
            r2Min=sys.maxsize if i+1>=n else nums2[i+1]
            r1Min=sys.maxsize if j+1>=m else nums1[j+1]
            
            if l2Max<=r1Min and l1Max<=r2Min:
                if (m+n)%2==0:
                    return (min(r1Min,r2Min)+max(l1Max,l2Max))/2
                else:
                    return min(r1Min,r2Min)
            elif l2Max>r1Min:
                e=i-1
            else:
                s=i+1

        return -1
        