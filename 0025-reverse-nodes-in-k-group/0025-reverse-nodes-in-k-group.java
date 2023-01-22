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
    public ListNode reverseKGroup(ListNode head, int k) {
        Stack<ListNode> st = new Stack<>();
        ListNode head2 = new ListNode();
        ListNode temp1 = head2;
        ListNode temp2 = null;
        while(head!=null){
            if(st.size()==0) temp2 = head;
            st.push(head);
            if(st.size()==k){
                while(!st.isEmpty()){
                    ListNode temp = new ListNode(st.pop().val);
                    head2.next = temp;
                    head2 = head2.next;
                }
            }
            head = head.next;
        }
        if(!st.isEmpty()) head2.next = temp2;
        return temp1.next;
    }
}