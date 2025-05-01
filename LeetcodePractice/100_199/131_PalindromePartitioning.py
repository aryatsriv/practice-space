#131. Palindrome Partitioning
#Solved
#Medium
#Topics
#Companies
#Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.
#
# 
#
#Example 1:
#
#Input: s = "aab"
#Output: [["a","a","b"],["aa","b"]]
#Example 2:
#
#Input: s = "a"
#Output: [["a"]]
# 
#
#Constraints:
#
#1 <= s.length <= 16
#s contains only lowercase English letters.

class Solution:
    def is_palindrome(self,s:str)->bool:
        l=0
        r=len(s)-1
        while l<r:
            if s[l]!=s[r]:
                return False
            l+=1
            r-=1
        return True

    def partition(self, s: str) -> List[List[str]]:
        if s=="":
            return [[]]
        n=len(s)
        res=[]
        curr=""
        for i in range(1,n+1):
            if self.is_palindrome(s[:i]):
                curr=s[:i]
                new_res=self.partition(s[i:])
                for item in new_res:
                    curr_res=[curr]
                    curr_res.extend(item)
                    res.append(curr_res)

        return res                    

        

