#
#72. Edit Distance
#Solved
#Medium
#Topics
#Companies
#Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.
#
#You have the following three operations permitted on a word:
#
#Insert a character
#Delete a character
#Replace a character
# 
#
#Example 1:
#
#Input: word1 = "horse", word2 = "ros"
#Output: 3
#Explanation: 
#horse -> rorse (replace 'h' with 'r')
#rorse -> rose (remove 'r')
#rose -> ros (remove 'e')
#Example 2:
#
#Input: word1 = "intention", word2 = "execution"
#Output: 5
#Explanation: 
#intention -> inention (remove 't')
#inention -> enention (replace 'i' with 'e')
#enention -> exention (replace 'n' with 'x')
#exention -> exection (replace 'n' with 'c')
#exection -> execution (insert 'u')
# 
#
#Constraints:
#
#0 <= word1.length, word2.length <= 500
#word1 and word2 consist of lowercase English letters.
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m=len(word1)
        n=len(word2)
        cache={}
        def rec(i,j):
            if j==n:
                return m-i
            if i==m:
                return n-j
            if (i,j) in cache:
                return cache[(i,j)]
            if word1[i]==word2[j]:
                cache[(i,j)]=rec(i+1,j+1)
                return cache[(i,j)]
            insert=1+rec(i,j+1)
            delete=1+rec(i+1,j)
            replace=1+rec(i+1,j+1)
            cache[(i,j)]= min(insert,delete,replace)
            return cache[(i,j)]
        
        return rec(0,0)
