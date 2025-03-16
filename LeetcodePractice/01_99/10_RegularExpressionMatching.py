#10. Regular Expression Matching
#Solved
#Hard
#Topics
#Companies
#Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:
#
#'.' Matches any single character.​​​​
#'*' Matches zero or more of the preceding element.
#The matching should cover the entire input string (not partial).
#
# 
#
#Example 1:
#
#Input: s = "aa", p = "a"
#Output: false
#Explanation: "a" does not match the entire string "aa".
#Example 2:
#
#Input: s = "aa", p = "a*"
#Output: true
#Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
#Example 3:
#
#Input: s = "ab", p = ".*"
#Output: true
#Explanation: ".*" means "zero or more (*) of any character (.)".
# 
#
#Constraints:
#
#1 <= s.length <= 20
#1 <= p.length <= 20
#s contains only lowercase English letters.
#p contains only lowercase English letters, '.', and '*'.
#It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m=len(s)
        n=len(p)
        def rec(i,j):
            if i==m and j==n:
                return True
            if j==n:
                return False
            
            match = i<m and (s[i]==p[j] or p[j]=='.')
            
            if j+1<n and p[j+1]=='*':
                return rec(i,j+2) or (match and rec(i+1,j))
            
            if match:
                return rec(i+1,j+1)
            
            return False

        return rec(0,0)
