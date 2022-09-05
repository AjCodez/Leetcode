"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    # def rec(self, root, )
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        q=collections.deque()
        if not root:
            return []
        q.append(root)
        ar=[[root.val]]
        while q:
            a=[]
            for i in range(len(q)):
                b=q.popleft()
                for i in b.children:
                    a.append(i.val)
                    if i:
                        q.append(i)
            ar.append(a)
        return ar[:len(ar)-1]