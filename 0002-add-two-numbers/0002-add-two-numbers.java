/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode head = new ListNode(-1);
        ListNode temp=head;
        int c=0;
        int s = 0;
        while(l1!=null || l2!=null){
            if(l1!=null) {
                s+=l1.val;
                l1=l1.next;
            }
            if(l2!=null) {
                s+=l2.val;
                l2=l2.next;
            }
            c=s/10;
            temp.next = new ListNode(s%10);
            s=c;
            temp=temp.next;
        }
        if(c>0) temp.next=new ListNode(c);
        return head.next;
    }
}