# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        l=[]
        for i in lists:
            temp=i
            while temp is not None:
                l.append(temp.val)
                temp=temp.next
        l.sort()
        sll=t=ListNode()
        for i in l:
            t.next=ListNode(i)
            t=t.next
        return sll.next