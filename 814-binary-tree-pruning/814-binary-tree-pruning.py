# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def pot(self,root):
    #     if not root:
    #         return None
    #     self.pot(root.left)
    #     self.pot(root.right)
    #     if not root.left and not root.right and root.val==0:
    #         return None
    #     return root
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        root.left=self.pruneTree(root.left)
        root.right=self.pruneTree(root.right)
        if not root.left and not root.right and root.val==0:
            return None
        return root