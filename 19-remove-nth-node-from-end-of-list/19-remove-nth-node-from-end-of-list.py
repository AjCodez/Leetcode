# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if n==1:
            if not head.next:
                return None
            temp=head
            while True:
                if not temp.next.next:
                    temp.next=temp.next.next
                    break
                temp=temp.next
            return head
        temp=head
        c=0
        while temp:
            c+=1
            temp=temp.next
        if c==n:
            return head.next
        n=c-n
        if n==1:
            head.next=head.next.next
            return head
        temp=head
        while True:
            temp=temp.next
            n-=1
            if n==1:
                temp.next=temp.next.next
                break
        return head