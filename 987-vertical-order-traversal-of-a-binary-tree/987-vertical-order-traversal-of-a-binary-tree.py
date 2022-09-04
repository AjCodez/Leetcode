# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preord(self, m, root, c, r):
        if not root:
            return
        if c in m:
            m[c].append((r,root.val))
        else:
            m[c]=[(r,root.val)]
        self.preord(m,root.left,c-1,r+1)
        self.preord(m,root.right,c+1,r+1)
        return
        
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        m={}
        c=0
        r=0
        m[c]=[(r,root.val)]
        self.preord(m,root.left,c-1,r+1)
        self.preord(m,root.right,c+1,r+1)
        a=[]
        for i in sorted(m):
            b=[]
            for j in sorted(m[i]):
                b.append(j[1])
            a.append(b)
            
        return a