"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    
    def trav(self,root,ar):
        
        if not root:
            return
        ar.append(root.val)
        for i in root.children:
            self.trav(i,ar)
        return
    
    def preorder(self, root: 'Node') -> List[int]:
        ar=[]
        self.trav(root,ar)
        return ar