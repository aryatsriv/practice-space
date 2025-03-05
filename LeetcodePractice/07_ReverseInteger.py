#7. Reverse Integer
#Solved
#Medium
#Topics
#Companies
#Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
#
#Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
#
# 
#
#Example 1:
#
#Input: x = 123
#Output: 321
#Example 2:
#
#Input: x = -123
#Output: -321
#Example 3:
#
#Input: x = 120
#Output: 21
# 
#
#Constraints:
#
#-231 <= x <= 231 - 1
class Solution:
    def reverse(self, x: int) -> int:
        res=0
        isNegative=-1 if x<0 else 1
        x=abs(x)

        while x>0:
            val=x%10
            x=x//10
            res=res*10+val
        
        res=res*isNegative
        if res<=math.pow(2,31) and res>-1*math.pow(2,31):
            return res
        
        return 0
