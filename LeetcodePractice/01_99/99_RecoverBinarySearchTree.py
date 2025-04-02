#99. Recover Binary Search Tree
#Medium
#Topics
#Companies
#You are given the root of a binary search tree (BST), where the values of exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.
#
# 
#
#Example 1:
#
#
#Input: root = [1,3,null,null,2]
#Output: [3,1,null,null,2]
#Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.
#Example 2:
#
#
#Input: root = [3,1,4,null,null,2]
#Output: [2,1,4,null,null,3]
#Explanation: 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2 and 3 makes the BST valid.
# 
#
#Constraints:
#
#The number of nodes in the tree is in the range [2, 1000].
#-231 <= Node.val <= 231 - 1
# 
#
#Follow up: A solution using O(n) space is pretty straight-forward. Could you devise a constant O(1) space solution?


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        prevNode = None
        first = None
        middle = None
        second = None
        
        #inorder traversal as it gives sorted output
        def dfs(node):
            nonlocal prevNode 
            nonlocal first
            nonlocal middle
            nonlocal second

            if node==None:
                return
            
            dfs(node.left)
            if prevNode and prevNode.val>node.val and first==None:
                first=prevNode
                middle=node
            elif prevNode and prevNode.val>node.val:
                second=node
            prevNode=node
            dfs(node.right)
            return node

        dfs(root)
        
        if second==None:
            second=middle
        first.val,second.val=second.val,first.val
        return root

        

    #using classic two numbers swapped in array 
    def recoverTreeClassic(self, root: Optional[TreeNode]) -> None:
        prevNode = None
        first = None
        middle = None
        second = None
        
        #inorder traversal as it gives sorted output
        def dfs(node):
            nonlocal prevNode 
            nonlocal first
            nonlocal second

            if node==None:
                return
            dfs(node.left)
            
            if prevNode and prevNode.val>node.val:
                second=node
                if first is None:
                    first=prevNode
            
            prevNode=node
            dfs(node.right)
            return node

        dfs(root)
        
        first.val,second.val=second.val,first.val
        return root

        
