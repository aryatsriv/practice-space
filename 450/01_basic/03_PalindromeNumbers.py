#9. Palindrome Number
#Solved
#Easy
#Topics
#conpanies icon
#Companies
#Hint
#Given an integer x, return true if x is a palindrome, and false otherwise.
#
# 
#
#Example 1:
#
#Input: x = 121
#Output: true
#Explanation: 121 reads as 121 from left to right and from right to left.
#Example 2:
#
#Input: x = -121
#Output: false
#Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
#Example 3:
#
#Input: x = 10
#Output: false
#Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
# 
#
#Constraints:
#
#-231 <= x <= 231 - 1
# 
#
#Follow up: Could you solve it without converting the integer to a string?


class Solution:
    def isPalindromeStr(self, y: int) -> bool:
        return str(y)==str(y)[::-1]
    
    def isPalindromeInt(self, y: int) -> bool:
        x=y
        if x<0:
            return False
        res=0

        while x>0:
            val=x%10
            x=x//10
            res=res*10+val

        print(res)
        return True if res==y else False
