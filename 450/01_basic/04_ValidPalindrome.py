#
#125. Valid Palindrome
#Solved
#Easy
#Topics
#conpanies icon
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

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        def rec(i,j):
            print(i,j,s[i],s[j])
            if i>=j:
                return True
            if s[i].isalnum()==False:
                return rec(i+1,j)
            if s[j].isalnum()==False:
                return rec(i,j-1)
            if s[i]==s[j]:
                return rec(i+1,j-1)
            return False
        
        return rec(0,len(s)-1)
        
