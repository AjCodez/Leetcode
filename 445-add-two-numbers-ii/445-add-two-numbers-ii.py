# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3=None
        l4=None
        
        l5=None
        
        while l1:
            temp=ListNode(l1.val)
            temp.next=l3
            l3=temp
            l1=l1.next
            
        while l2:
            temp=ListNode(l2.val)
            temp.next=l4
            l4=temp
            l2=l2.next
        
        
        c=0
        while l3 or l4:
            if l3 and l4:
                temp=ListNode((l3.val+l4.val+c)%10)
                temp.next=l5
                l5=temp
                c=(l3.val+l4.val+c)//10
            elif l3:
                temp=ListNode((l3.val+c)%10)
                temp.next=l5
                l5=temp
                c=(l3.val+c)//10
            elif l4:
                temp=ListNode((l4.val+c)%10)
                temp.next=l5
                l5=temp
                c=(l4.val+c)//10
            if l3:
                l3=l3.next
            if l4:
                l4=l4.next
        if c:
            temp=ListNode(c)
            temp.next=l5
            l5=temp
        return l5