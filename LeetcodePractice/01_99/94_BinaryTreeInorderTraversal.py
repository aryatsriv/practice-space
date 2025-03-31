#94. Binary Tree Inorder Traversal
#Easy
#Topics
#Companies
#Given the root of a binary tree, return the inorder traversal of its nodes' values.
#
# 
#
#Example 1:
#
#Input: root = [1,null,2,3]
#
#Output: [1,3,2]
#
#Explanation:
#
#
#
#Example 2:
#
#Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
#
#Output: [4,2,6,5,7,1,3,9,8]
#
#Explanation:
#
#
#
#Example 3:
#
#Input: root = []
#
#Output: []
#
#Example 4:
#
#Input: root = [1]
#
#Output: [1]
#
# 
#
#Constraints:
#
#The number of nodes in the tree is in the range [0, 100].
#-100 <= Node.val <= 100
# 
#
#Follow up: Recursive solution is trivial, could you do it iteratively?

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        if root==None:
            return res

        def rec(node):
            if node==None:
                return
            rec(node.left)
            res.append(node.val)
            rec(node.right)
        
        rec(root)
        return res

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        st=[]
        node=root
        while node or st:
            if node!=None: 
                st.append(node)
                node=node.left
            else:
                temp=st.pop()
                res.append(temp.val)
                node=temp.right
        
        return res
