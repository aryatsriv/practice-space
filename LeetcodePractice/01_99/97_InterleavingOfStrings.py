#97. Interleaving String
#Solved
#Medium
#Topics
#Companies
#Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.
#
#An interleaving of two strings s and t is a configuration where s and t are divided into n and m substrings respectively, such that:
#
#s = s1 + s2 + ... + sn
#t = t1 + t2 + ... + tm
#|n - m| <= 1
#The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
#Note: a + b is the concatenation of strings a and b.
#
# 
#
#Example 1:
#
#
#Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
#Output: true
#Explanation: One way to obtain s3 is:
#Split s1 into s1 = "aa" + "bc" + "c", and s2 into s2 = "dbbc" + "a".
#Interleaving the two splits, we get "aa" + "dbbc" + "bc" + "a" + "c" = "aadbbcbcac".
#Since s3 can be obtained by interleaving s1 and s2, we return true.
#Example 2:
#
#Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
#Output: false
#Explanation: Notice how it is impossible to interleave s2 with any other string to obtain s3.
#Example 3:
#
#Input: s1 = "", s2 = "", s3 = ""
#Output: true
# 
#
#Constraints:
#
#0 <= s1.length, s2.length <= 100
#0 <= s3.length <= 200
#s1, s2, and s3 consist of lowercase English letters.
# 
#
#Follow up: Could you solve it using only O(s2.length) additional memory space?
#
class Solution:

    def isInterleaveIterative(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3)!=(len(s1)+len(s2)):
            return False
        cache =[[False for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
        cache[0][0]=True
        
        for i in range(1,len(s2)+1):
            if s2[i-1]==s3[i-1]:
                cache[0][i]=True
            else:
                break
        
        for i in range(1,len(s1)+1):
            if cache[i-1][0] and s1[i-1]==s3[i-1]:
                cache[i][0]=True 
            for j in range(1,len(s2)+1):
                charS1=s1[i-1]
                charS2=s2[j-1]
                charS3=s3[i+j-1]
                ilS1=False
                ilS2=False

                if charS3==charS1:
                    ilS1=cache[i-1][j]
                if charS3==charS2:
                    ilS2=cache[i][j-1]
                cache[i][j] = ilS1 or ilS2

        
        return cache[len(s1)][len(s2)]



    def isInterleaveWithoutIndexForS3(self, s1: str, s2: str, s3: str) -> bool:
        i=0
        j=0
        k=0
        cache={}
        def rec(i,j):
            if (i+j)>=len(s3) and i>=len(s1) and j>=len(s2):
                return True
            if (i+j)>=len(s3):
                return False

            if (i,j) in cache:
                return cache[(i,j)]
            
            c1='A' if i>=len(s1) else s1[i]
            c2='A' if j>=len(s2) else s2[j]
            c3=s3[i+j]
            left=False
            right=False
            if c3==c1:
                left=rec(i+1,j)
            if c3==c2:
                right=rec(i,j+1)
            
            if c3!=c1 and c3!=c2:
                cache[(i,j)]= False

            cache[(i,j)]= left or right
            return cache[(i,j)]

        return rec(0,0)

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        i=0
        j=0
        k=0
        cache={}
        def rec(i,j,k):
            if k>=len(s3) and i>=len(s1) and j>=len(s2):
                return True
            if k>=len(s3):
                return False
            if (i,j,k) in cache:
                return cache[(i,j,k)]
            c1='A' if i>=len(s1) else s1[i]
            c2='A' if j>=len(s2) else s2[j]
            c3=s3[k]
            left=False
            right=False
            if c3==c1:
                left=rec(i+1,j,k+1)
            if c3==c2:
                right=rec(i,j+1,k+1)
            
            if c3!=c1 and c3!=c2:
                cache[(i,j,k)]= False

            cache[(i,j,k)]= left or right
            return cache[(i,j,k)]
            
        return rec(0,0,0)

