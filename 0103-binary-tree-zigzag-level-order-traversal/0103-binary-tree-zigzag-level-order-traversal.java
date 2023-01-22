/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        Deque<TreeNode> dq = new LinkedList<>();
        List<List<Integer>> arr = new ArrayList<>();
        if(root==null) return arr;
        boolean lvl = true;
        dq.addLast(root);
        while(!dq.isEmpty()){
            List<Integer> ar = new ArrayList<>();
            int n = dq.size();
            for(int i=0;i<n;i++){
                if(lvl){
                    TreeNode temp = dq.removeFirst();
                    if(temp.left!=null) dq.addLast(temp.left);
                    if(temp.right!=null) dq.addLast(temp.right);
                    ar.add(temp.val);
                }
                else{
                    TreeNode temp = dq.removeLast();
                    if(temp.right!=null) dq.addFirst(temp.right);
                    if(temp.left!=null) dq.addFirst(temp.left);
                    ar.add(temp.val);
                }
            }
            arr.add(ar);
            lvl=!lvl;
        }
        return arr;
    }
}