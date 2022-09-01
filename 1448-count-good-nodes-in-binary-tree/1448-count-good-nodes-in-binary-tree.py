# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode, m=-math.inf) -> int:
        count=0
        if not root:
            return 0
        if m<=root.val:
            m=root.val
            count+=1
        count+=self.goodNodes(root.right,m)+self.goodNodes(root.left,m)
        return count