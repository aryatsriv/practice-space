#
#132. Palindrome Partitioning II
#Hard
#Topics
#Companies
#Given a string s, partition s such that every substring of the partition is a palindrome.
#
#Return the minimum cuts needed for a palindrome partitioning of s.
#
# 
#
#Example 1:
#
#Input: s = "aab"
#Output: 1
#Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
#Example 2:
#
#Input: s = "a"
#Output: 0
#Example 3:
#
#Input: s = "ab"
#Output: 1

class Solution:
    def is_palindrome(self,s,l,r):
        while l<r:
            if s[l]!=s[r]:
                return False
            l+=1
            r-=1
        return True

    def minCut(self, s: str) -> int:
        n=len(s)
        cache={}
        def rec(i):
            if i>=n:
                return 0
            min_val=sys.maxsize
            for j in range(i,n):
                if self.is_palindrome(s,i,j):
                    min_val=min(min_val,1+rec(j+1))

            cache[i]= min_val    
            return cache[i]

        return rec(0)-1
