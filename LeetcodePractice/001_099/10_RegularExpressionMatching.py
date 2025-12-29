# 10. Regular Expression Matching
# Solved
# Hard
# Topics
# premium lock icon
# Companies
# Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:
#
# '.' Matches any single character.​​​​
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).
#
#
#
# Example 1:
#
# Input: s = "aa", p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
# Example 2:
#
# Input: s = "aa", p = "a*"
# Output: true
# Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
# Example 3:
#
# Input: s = "ab", p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".
#
#
# Constraints:
#
# 1 <= s.length <= 20
# 1 <= p.length <= 20
# s contains only lowercase English letters.
# p contains only lowercase English letters, '.', and '*'.
# It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m=len(s)
        n=len(p)
        cache={}
        def rec(i,j):
            if (i,j) in cache:
                return cache[(i,j)]
            if i>=m and j>=n:
                return True
            elif j>=n:
                return False
            
            res=False

            if i>=m and j+1<n and p[j+1]=='*':
                res=rec(i,j+2)
            elif i>=m:
                res=False
            elif (s[i]==p[j] or p[j]=='.') and (j+1>=n or p[j+1]!='*'):
                res=rec(i+1,j+1)
            elif j+1<n and p[j+1]=='*' and (s[i]==p[j] or p[j]=='.'):
                res=rec(i+1,j) or rec(i,j+2)
            elif j+1<n and p[j+1]=='*' and s[i]!=p[j]:
                res=rec(i,j+2)

            cache[(i,j)]= res
            return cache[(i,j)]

        return rec(0,0)
