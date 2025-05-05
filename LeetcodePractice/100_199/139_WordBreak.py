#139. Word Break
#Solved
#Medium
#Topics
#Companies
#Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.
#
#Note that the same word in the dictionary may be reused multiple times in the segmentation.
#
# 
#
#Example 1:
#
#Input: s = "leetcode", wordDict = ["leet","code"]
#Output: true
#Explanation: Return true because "leetcode" can be segmented as "leet code".
#Example 2:
#
#Input: s = "applepenapple", wordDict = ["apple","pen"]
#Output: true
#Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
#Note that you are allowed to reuse a dictionary word.
#Example 3:
#
#Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
#Output: false
# 
#
#Constraints:
#
#1 <= s.length <= 300
#1 <= wordDict.length <= 1000
#1 <= wordDict[i].length <= 20
#s and wordDict[i] consist of only lowercase English letters.
#All the strings of wordDict are unique.

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set=set(wordDict)
        n=len(s)
        cache={}
        def rec(i):
            if i in cache:
                return cache[i]
            if i>=n:
                return True
            for j in range(i,n):
                word=s[i:j+1]
                if word in word_set:
                    if rec(j+1):
                        cache[i]= True
                        return cache[i]
                    
            cache[i]= False
            return cache[i]

        return rec(0)

