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
    static int s=0;
    private void trav(TreeNode root,int low, int high){
        if (root==null) return;
        if (root.val>=low && root.val<=high) s+=root.val;
        trav(root.right,low,high);
        trav(root.left,low,high);
    }
    
    public int rangeSumBST(TreeNode root, int low, int high) {
        s=0;
        trav(root,low,high);
        return s;
    }
}