# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr=[]
        temp=head
        while temp:
            arr.append(temp.val)
            temp=temp.next
        n1=0
        n2=len(arr)-1
        while n1<len(arr)/2:
            if arr[n1]!=arr[n2]:
                return False
            n1+=1
            n2-=1
        return True