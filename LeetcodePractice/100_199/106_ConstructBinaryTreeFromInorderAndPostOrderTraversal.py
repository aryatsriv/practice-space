#105. Construct Binary Tree from Preorder and Inorder Traversal
#Solved
#Medium
#Topics
#Companies
#Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.
#
# 
#
#Example 1:
#
#
#Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
#Output: [3,9,20,null,null,15,7]
#Example 2:
#
#Input: preorder = [-1], inorder = [-1]
#Output: [-1]
# 
#
#Constraints:
#
#1 <= preorder.length <= 3000
#inorder.length == preorder.length
#-3000 <= preorder[i], inorder[i] <= 3000
#preorder and inorder consist of unique values.
#Each value of inorder also appears in preorder.
#preorder is guaranteed to be the preorder traversal of the tree.
#inorder is guaranteed to be the inorder traversal of the tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not postorder or not inorder:
            return None
        n=len(postorder)
        root=TreeNode(postorder[n-1])
        mid=inorder.index(root.val)
        root.left=self.buildTree(inorder[0:mid],postorder[0:mid])
        root.right=self.buildTree(inorder[mid+1:n],postorder[mid:n-1])
        return root
