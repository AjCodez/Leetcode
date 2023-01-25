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
    
    public boolean isBalanced(TreeNode root){
        return isBalance(root).isBalanced;
    }
    
    private BalancedPair isBalance(TreeNode node) {
        
			if (node==null) return new BalancedPair();

            BalancedPair lbp = isBalance(node.left);
            BalancedPair rbp = isBalance(node.right);
            BalancedPair cbp = new BalancedPair();

            cbp.isBalanced = lbp.isBalanced && rbp.isBalanced && Math.abs(lbp.height-rbp.height)<=1;
            cbp.height = Math.max(lbp.height,rbp.height)+1;
            return cbp;
			
		}

		private class BalancedPair {
			int height = -1;
			boolean isBalanced = true;
		}
}