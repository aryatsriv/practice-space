#14. Longest Common Prefix
#Solved
#Easy
#Topics
#Companies
#Write a function to find the longest common prefix string amongst an array of strings.
#
#If there is no common prefix, return an empty string "".
#
# 
#
#Example 1:
#
#Input: strs = ["flower","flow","flight"]
#Output: "fl"
#Example 2:
#
#Input: strs = ["dog","racecar","car"]
#Output: ""
#Explanation: There is no common prefix among the input strings.
# 
#
#Constraints:
#
#1 <= strs.length <= 200
#0 <= strs[i].length <= 200
#strs[i] consists of only lowercase English letters if it is non-empty.
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        j=0
        m=len(strs[0])

        while j<m:
            c=strs[0][j]
            for word in strs:
                if j>=len(word) or word[j]!=c:
                    return word[0:j]
            j+=1

        return strs[0]    
            
