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
    private int findLeaf(Stack<TreeNode> s){
        while(true){
            TreeNode n = s.pop();
            if(n.left!=null) s.push(n.left);
            if(n.right!=null) s.push(n.right);
            if(n.right==null && n.left==null) return n.val;
        }
    }
    
    public boolean leafSimilar(TreeNode root1, TreeNode root2) {
        Stack<TreeNode> s1=new Stack<>(), s2= new Stack<>();
        s1.push(root1);
        s2.push(root2);
        while(!s1.empty() && !s2.empty()){
            if(findLeaf(s1)!=findLeaf(s2)) return false;
        }
        return s1.empty() && s2.empty();
    }
}