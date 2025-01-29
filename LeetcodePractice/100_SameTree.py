# 100. Same Tree
# Solved
# Easy
# Topics
# Companies
# Given the roots of two binary trees p and q, write a function to check if they are the same or not.
# 
# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
# 
#  
# 
# Example 1:
# 
# 
# Input: p = [1,2,3], q = [1,2,3]
# Output: true
# Example 2:
# 
# 
# Input: p = [1,2], q = [1,null,2]
# Output: false
# Example 3:
# 
# 
# Input: p = [1,2,1], q = [1,1,2]
# Output: false
#  
# 
# Constraints:
# 
# The number of nodes in both trees is in the range [0, 100].
# -104 <= Node.val <= 104
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        l=p
        r=q
        def rec(l,r):
            if l==None and r==None:
                return True
            elif l==None or r==None:
                return False
            elif l.val==r.val:
                return rec(l.left,r.left) and rec(l.right,r.right)
            else:
                return False


        return rec(l,r)
            