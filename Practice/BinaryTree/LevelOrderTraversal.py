# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return None

        q = deque()
        q.append(root)
        res=[]
        while len(q) != 0:
            levelRes=[]
            
            size = len(q)
            
            for i in range(size):
                node = q.popleft()
                levelRes.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            res.append(levelRes)
        
        return res    
