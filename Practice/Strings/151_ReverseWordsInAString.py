class Solution:
    def reverseWords(self, s: str) -> str:
        res=""
        i=len(s)-1
        
        
        while i>=0:
            j=i
            curr=""
            while j>=0 and s[j]!=' ':
                j=j-1
            if j<i:
                curr=s[j+1:i+1]
            i=j
            if j>=0 and s[j]==' ':
                while j>=0 and s[j]==' ':
                    j=j-1

                if (i+1)<len(s) and j>=0:
                    curr+=" "

            res=res+curr
            i=j
        
        return res
