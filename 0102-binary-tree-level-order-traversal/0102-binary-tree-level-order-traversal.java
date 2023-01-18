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
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> arr = new ArrayList<>();
        if(root==null) return arr;
        List<Integer> l = new ArrayList<>();
        Queue<TreeNode> q1 = new LinkedList<>();
        Queue<TreeNode> q2 = new LinkedList<>();
        q1.offer(root);
        while(!q1.isEmpty()){
            TreeNode temp = q1.poll();
            l.add(temp.val);
            if(temp.left!=null) q2.offer(temp.left);
            if(temp.right!=null) q2.offer(temp.right);
            if(q1.isEmpty()){
                arr.add(l);
                l = new ArrayList<>();
                q1=q2;
                q2 = new LinkedList<>();
            }
        }
        return arr;
    }
}