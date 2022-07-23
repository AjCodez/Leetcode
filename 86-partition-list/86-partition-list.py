# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # def check(self, head: Optional[ListNode], x: int) -> bool:
    #     while head.next:
    #         if head.val>=x and head.next.val<x:
    #             return False
    #         else:
    #             head=head.next
    #     else:
    #         return True
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head is None:
            return None
        l=less = ListNode()
        m=more = ListNode()
        while head:
            if head.val<x:
                less.next = head
                less = less.next
            else:
                more.next = head
                more = more.next
            head = head.next
        less.next, more.next = m.next, None
        return l.next