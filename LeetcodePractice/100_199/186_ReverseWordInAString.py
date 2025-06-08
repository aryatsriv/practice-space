#186. Reverse Words in a String II
#Medium
#Topics
#Companies
#Given a character array s, reverse the order of the words.
#
#A word is defined as a sequence of non-space characters. The words in s will be separated by a single space.
#
#Your code must solve the problem in-place, i.e. without allocating extra space.
#
# 
#
#Example 1:
#
#Input: s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
#Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
#Example 2:
#
#Input: s = ["a"]
#Output: ["a"]
# 
#
#Constraints:
#
#1 <= s.length <= 105
#s[i] is an English letter (uppercase or lowercase), digit, or space ' '.
#There is at least one word in s.
#s does not contain leading or trailing spaces.
#All the words in s are guaranteed to be separated by a single space.


class Solution:
    def reverseWords(self, s: List[str]) -> None:
        if len(s)==0:
            return
        s.reverse()
        
        i=0
        j=0
        n=len(s)

        while j<n:
            if s[j]==' ':
                k=j-1
                while i<k:
                    s[i],s[k]=s[k],s[i]
                    i+=1
                    k-=1
                while s[j]==' ':
                    j+=1
                i=j
            elif j==n-1:
                k=j
                while i<k:
                    s[i],s[k]=s[k],s[i]
                    i+=1
                    k-=1
                j+=1
            else:
                j+=1
            
            

        
