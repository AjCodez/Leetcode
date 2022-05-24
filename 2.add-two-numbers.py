#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = c = ListNode(0)
        carr = 0
        while l1 or l2:
            v = carr
            if l1:
                v+=l1.val
                l1=l1.next
            if l2:
                v+=l2.val
                l2=l2.next
            c.next = ListNode(v%10)
            c=c.next
            carr = v//10
        if carr>0:
            c.next = ListNode(carr)
        return head.next
# @lc code=end

