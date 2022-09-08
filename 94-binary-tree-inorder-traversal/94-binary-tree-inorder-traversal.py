# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def iot(self,root,ar):
        if not root:
            return
        self.iot(root.left,ar)
        ar.append(root.val)
        self.iot(root.right,ar)
        return 
    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ar=[]
        self.iot(root,ar)
        return ar