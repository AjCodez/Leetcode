# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNode(self, head):
        if not head or not head.next:
            return head
        temp=head.val
        head.val = head.next.val
        head.next.val = temp
        return self.swapNode(head.next.next)
    
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        self.swapNode(temp)
        return head
            