# 4. Median of Two Sorted Arrays
# Solved
# Hard
# Topics
# conpanies icon
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
    #O(Log(n+m) time)
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums2)>len(nums1):
            return self.findMedianSortedArrays(nums2,nums1)

        
        l1,l2,r1,r2=0,0,len(nums1)-1,len(nums2)-1
        half=(len(nums1)+len(nums2))//2
        while True:
            mid=(l2+r2)//2
            l1Max=half-mid-2
            l1Val=-sys.maxsize if l1Max<0 else nums1[l1Max]
            l2Val=-sys.maxsize if mid<0 else nums2[mid]
            r1Val=sys.maxsize if l1Max+1 >=len(nums1) else nums1[l1Max+1]
            r2Val=sys.maxsize if mid+1>=len(nums2) else nums2[mid+1]

            if l1Val<=r2Val and l2Val<=r1Val:
                if (len(nums1)+len(nums2))%2==0:
                    return (max(l1Val,l2Val)+min(r1Val,r2Val))/2
                return min(r1Val,r2Val)
            elif l1Val>r2Val:
                l2=mid+1
            else:
                r2=mid-1

        

        return -1
    #Linear Time O(n+m)
    def findMedianSortedArraysInLinearTime(self, nums1: List[int], nums2: List[int]) -> float:
        i=0
        j=0

        m=len(nums1)
        n=len(nums2)
        
        m2=(m+n)//2
        m1=(m+n-1)//2

        k=0
        res1=0
        res2=0
        while i<m and j<n:
            val=0
            if nums1[i]<nums2[j]:
                val=nums1[i]
                i+=1
            else:
                val=nums2[j]
                j+=1
            if k==m1:
                res1=val
            if k==m2:
                res2=val
                k+=1
                break
            k+=1

        while i<m and k<=m2:
            val=nums1[i]
            if k==m1:
                res1=val
            if k==m2:
                res2=val
                break
            i+=1
            k+=1

        while j<n and k<=m2:
            val=nums2[j]
            if k==m1:
                res1=val
            if k==m2:
                res2=val
                break
            j+=1
            k+=1

      
        return (res1+res2)/2

