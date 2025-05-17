#159. Longest Substring with At Most Two Distinct Characters
#Medium
#Topics
#Companies
#Given a string s, return the length of the longest substring that contains at most two distinct characters.
#
# 
#
#Example 1:
#
#Input: s = "eceba"
#Output: 3
#Explanation: The substring is "ece" which its length is 3.
#Example 2:
#
#Input: s = "ccaabbb"
#Output: 5
#Explanation: The substring is "aabbb" which its length is 5.
# 
#
#Constraints:
#
#1 <= s.length <= 105
#s consists of English letters.


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
    # have a dict to store values and count
    # have a maxlenth which would be res
    # s and e - calculate maxlength in each iteration - lets see if we can find a way to calculate in each iteration
        cache=defaultdict(int)
        res=0
        l=0
        n=len(s)
        
        for i in range(n):
            cache[s[i]]+=1
            while len(cache)>2:
                cache[s[l]]-=1
                if cache[s[l]]==0:
                    del cache[s[l]]
                l+=1
            res=max(res,i-l+1)
        
        return res

