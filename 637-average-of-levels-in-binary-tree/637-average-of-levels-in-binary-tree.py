# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        arr=[]
        q=[]
        if root is None:
            return q
        q=[root]
        while q:
            s=0
            n=len(q)
            for i in range(n):
                a=q.pop(0)
                s+=a.val
                if a.left:
                    q.append(a.left)
                if a.right:
                    q.append(a.right)
            arr.append(s/n)
        return arr