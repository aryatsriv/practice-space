#67. Add Binary
#Easy
#Topics
#Companies
#Given two binary strings a and b, return their sum as a binary string.
#
# 
#
#Example 1:
#
#Input: a = "11", b = "1"
#Output: "100"
#Example 2:
#
#Input: a = "1010", b = "1011"
#Output: "10101"
# 
#
#Constraints:
#
#1 <= a.length, b.length <= 104
#a and b consist only of '0' or '1' characters.
#Each string does not contain leading zeros except for the zero itself.


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry=0
        m,n=len(a)-1,len(b)-1
        res=[]
        while m>=0 or n>=0 or carry>0:
            aval=0 if m<0 else int(a[m])
            bval=0 if n<0 else int(b[n])
            val=aval+bval+carry
            if val==0 or val==1:
                res.append(val)
                carry=0
            elif val==2:
                res.append(0)
                carry=1
            else:
                res.append(1)
                carry=1
            m-=1
            n-=1
        
        res.reverse()

        return "".join(map(str,res))
