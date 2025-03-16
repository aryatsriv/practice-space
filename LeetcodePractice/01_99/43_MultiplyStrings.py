#
#43. Multiply Strings
#Solved
#Medium
#Topics
#Companies
#Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.
#
#Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.
#
# 
#
#Example 1:
#
#Input: num1 = "2", num2 = "3"
#Output: "6"
#Example 2:
#
#Input: num1 = "123", num2 = "456"
#Output: "56088"
# 
#
#Constraints:
#
#1 <= num1.length, num2.length <= 200
#num1 and num2 consist of digits only.
#Both num1 and num2 do not contain any leading zero, except the number 0 itself.

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1=len(num1)
        n2=len(num2)
        n=n1+n2
        res=[]

        for i in range(n1-1,-1,-1):
            curr=[0]*n
            ind=n-1-(n1-1-i)
            carry=0
            for j in range(n2-1,-1,-1):
                val=int(num1[i])*int(num2[j])+carry
                curr[ind]=val%10
                carry=val//10
                ind-=1
            if carry>0:
                curr[ind]=carry
            res.append(curr)


        finalRes=[0]*n
        carry=0
        for i in range(n-1,-1,-1):
            sum=carry
            for val in res:
                sum+=val[i]
            finalRes[i]=sum%10
            carry=sum//10

        for i in range(0,n):
            if finalRes[i]!=0:
                return "".join(map(str,finalRes[i:]))

        return "" if n==0 else "0"
