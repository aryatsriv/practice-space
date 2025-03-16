#103. Binary Tree Zigzag Level Order Traversal
#Solved
#Medium
#Topics
#Companies
#Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).
#
# 
#
#Example 1:
#
#
#Input: root = [3,9,20,null,null,15,7]
#Output: [[3],[20,9],[15,7]]
#Example 2:
#
#Input: root = [1]
#Output: [[1]]
#Example 3:
#
#Input: root = []
#Output: []
# 
#
#Constraints:
#
#The number of nodes in the tree is in the range [0, 2000].
#-100 <= Node.val <= 100
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root==None:
            return []
        res=[]
        q=deque()
        q.append(root)
        reverse=False
        while q:
            n=len(q)
            curr=[]
            for i in range(n):
                temp=q.popleft()
                curr.append(temp.val)
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
            
            if reverse:
                curr.reverse()
            res.append(curr)
            reverse= not reverse
        
        return res
