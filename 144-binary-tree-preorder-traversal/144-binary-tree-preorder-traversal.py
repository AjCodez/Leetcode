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
        ar.append(root.val)
        self.pot(root.left,ar)
        self.pot(root.right,ar)
        return 
    
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ar=[]
        self.pot(root,ar)
        return ar