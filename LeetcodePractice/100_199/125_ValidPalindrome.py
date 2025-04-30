#125. Valid Palindrome
#Solved
#Easy
#Topics
#Companies
#A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
#
#Given a string s, return true if it is a palindrome, or false otherwise.
#
# 
#
#Example 1:
#
#Input: s = "A man, a plan, a canal: Panama"
#Output: true
#Explanation: "amanaplanacanalpanama" is a palindrome.
#Example 2:
#
#Input: s = "race a car"
#Output: false
#Explanation: "raceacar" is not a palindrome.
#Example 3:
#
#Input: s = " "
#Output: true
#Explanation: s is an empty string "" after removing non-alphanumeric characters.
#Since an empty string reads the same forward and backward, it is a palindrome.
# 
#
#Constraints:
#
#1 <= s.length <= 2 * 105
#s consists only of printable ASCII characters

class Solution:
    def is_alphabet(self,c)->bool:
        if (ord(c)-ord('a')>=0 and ord(c)-ord('a')<26) or (ord(c)-ord('0')>=0 and ord(c)-ord('0')<=9):
            return True
        return False
    def isPalindrome(self, s: str) -> bool:
        l=0
        r=len(s)-1
        s=s.lower()
        while l<r:
            if self.is_alphabet(s[l])==False:
                l+=1
                continue
            if self.is_alphabet(s[r])==False:
                r-=1
                continue
            if s[r]!=s[l]:
                return False
            l+=1
            r-=1
        
        return True
