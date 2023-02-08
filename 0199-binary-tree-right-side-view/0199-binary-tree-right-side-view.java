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
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> ls = new ArrayList<>();
        Queue<TreeNode> q =new LinkedList<>();
        if(root==null) return ls;
        q.offer(root);
        int n=root.val;
        while(!q.isEmpty()){
            int s = q.size();
            for(int i=0;i<s;i++){
                TreeNode temp = q.poll();
                n=temp.val;
                if(temp.left!=null) q.offer(temp.left);
                if(temp.right!=null) q.offer(temp.right);
            }
            ls.add(n);
        }
        return ls;
    }
}