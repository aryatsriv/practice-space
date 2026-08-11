# 5. Longest Palindromic Substring
# Medium
# Given a string s, return the longest palindromic substring in s.

 

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"
 

# Constraints:

# 1 <= s.length <= 1000
# s consist of only digits and English letters.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)==0:
            return ""
        print("here")
        res=0
        res_i=0
        res_j=0
        i=0
        s_len=len(s)

        while i<s_len:
            l,m=i,i

            while l>=0 and m<s_len and s[l]==s[m]:
                if (m-l+1)>res:
                    res=m-l+1
                    res_i=l
                    res_j=m+1
                l-=1
                m+=1
            
            l,m=i,i+1
            while l>=0 and m<s_len and s[l]==s[m]:
                if (m-l+1)>res:
                    res=m-l+1
                    res_i=l
                    res_j=m+1

                l-=1
                m+=1
            i+=1

        return s[res_i:res_j]      

