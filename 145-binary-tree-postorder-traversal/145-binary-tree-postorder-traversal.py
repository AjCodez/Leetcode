# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def pot(self,root,ar):
        if not root:
            return
        self.pot(root.left,ar)
        self.pot(root.right,ar)
        ar.append(root.val)
        return 
    
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ar=[]
        self.pot(root,ar)
        return ar