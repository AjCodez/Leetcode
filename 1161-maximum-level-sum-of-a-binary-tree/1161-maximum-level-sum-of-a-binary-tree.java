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
    public int maxLevelSum(TreeNode root) {
        int lvl=0;
        int ms = root.val;
        int ml = 1;
        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);
        while(!q.isEmpty()){
            int s = 0;
            lvl++;
            int size = q.size();
            for(int i=0;i<size;i++){
                TreeNode temp = q.remove();
                if(temp.left!=null) q.add(temp.left);
                if(temp.right!=null) q.add(temp.right);
                s+=temp.val;
            }
            if(s>ms){
                ms= s;
                ml = lvl;
            }
        }
        return ml;
    }
}