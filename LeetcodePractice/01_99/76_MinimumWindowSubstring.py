#
#76. Minimum Window Substring
#Solved
#Hard
#Topics
#Companies
#Hint
#Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".
#
#The testcases will be generated such that the answer is unique.
#
# 
#
#Example 1:
#
#Input: s = "ADOBECODEBANC", t = "ABC"
#Output: "BANC"
#Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
#Example 2:
#
#Input: s = "a", t = "a"
#Output: "a"
#Explanation: The entire string s is the minimum window.
#Example 3:
#
#Input: s = "a", t = "aa"
#Output: ""
#Explanation: Both 'a's from t must be included in the window.
#Since the largest window of s only has one 'a', return empty string.
# 
#
#Constraints:
#
#m == s.length
#n == t.length
#1 <= m, n <= 105
#s and t consist of uppercase and lowercase English letters.

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cacheT=Counter(t)
        m=len(s)
        n=len(t)
        left=0
        right=m+1
        i=0
        j=0
        cacheS=defaultdict(int)

        while j<m:
            cacheS[s[j]]+=1
            if s[j] in cacheT and cacheS[s[j]]==cacheT[s[j]]:
                allKeysPresent=True
                for key,value in cacheT.items():
                    if key not in cacheS or (key in cacheS and cacheS[key]<cacheT[key]):
                            allKeysPresent=False

                
                while allKeysPresent:
                    if (j-i)<right-left:
                        right=j
                        left=i
                    cacheS[s[i]]-=1
                    if cacheS[s[i]]==0:
                        del cacheS[s[i]]
                    i+=1
                    for key,value in cacheT.items():
                        if key not in cacheS or (key in cacheS and cacheS[key]<cacheT[key]):
                            allKeysPresent=False
            j+=1

        if right>len(s):
            return ""
        return s[left:right+1]
        
        

