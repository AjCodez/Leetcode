# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        
        q=collections.deque()
        q.append(root)
        ar=[]
        while q:
            a=[]
            for i in range(len(q)):
                b=q.popleft()
                a.append(b.val)
                if b.left:
                    q.append(b.left)
                if b.right:
                    q.append(b.right)
            ar.append(a)
        return ar[::-1]