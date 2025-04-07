#96. Unique Binary Search Trees
#Medium
#Topics
#Companies
#Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.
#
# 
#
#Example 1:
#
#
#Input: n = 3
#Output: 5
#Example 2:
#
#Input: n = 1
#Output: 1
# 
#
#Constraints:
#
#1 <= n <= 19


class Solution:
    def numTreesRec(self, n: int) -> int:
        cache={}
        def rec(i):
            if i==0 or i==1:
                return 1
            if i in cache:
                return cache[i]
            count=0
            for j in range(1,i+1):
                count+=rec(j-1)*rec(i-j)    
            cache[i]=count
            return cache[i]

        return rec(n) 

    def numTrees(self, n: int) -> int:
        cache={0:1,1:1}
        for i in range(2,n+1):
            count=0
            for j in range(1,i+1):
                count+=cache[j-1]*cache[i-j]    
            cache[i]=count

        return cache[n]
