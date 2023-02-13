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
    public TreeNode reverseOddLevels(TreeNode root) {
        boolean f = false;
        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);
        while(!q.isEmpty()){
            f=!f;
            int s = q.size();
            TreeNode t[] = new TreeNode[s];
            for(int i = 0; i<s; i++){
                TreeNode temp = q.remove();
                t[i]= temp;
                if(temp.left!=null){
                    q.add(temp.left);
                    q.add(temp.right);
                }
            }
            if(!f){
                for(int i =0, j=t.length-1;i<j;i++,j--){
                    int temp = t[i].val;
                    t[i].val = t[j].val;
                    t[j].val = temp;
                }
            }
        }
        return root;
    }
}