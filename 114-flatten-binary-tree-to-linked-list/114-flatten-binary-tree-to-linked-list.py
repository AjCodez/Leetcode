# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return
        s=[root]
        while len(s)!=0:
            curr = s.pop()
            if curr.right:
                s.append(curr.right)
            if curr.left:
                s.append(curr.left)
            if len(s)!=0:
                curr.right = s[-1]
            curr.left=None