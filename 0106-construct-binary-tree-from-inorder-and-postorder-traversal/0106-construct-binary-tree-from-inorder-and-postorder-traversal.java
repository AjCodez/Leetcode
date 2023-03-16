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
    public TreeNode buildTree(int[] inorder, int[] postorder) {
        TreeNode ret = new TreeNode(), p = ret;
        Deque<TreeNode> stk = new ArrayDeque<>();
        int i = inorder.length-1, j = postorder.length-1;
        while (j >= 0) {
            p.left = new TreeNode(postorder[j]);
            p = p.left;
            stk.push(p);
            while (postorder[j] != inorder[i]) {
                p.right = new TreeNode(postorder[--j]);
                p = p.right;
                stk.push(p);
            }
            j--;
            while (!stk.isEmpty() && stk.peek().val == inorder[i]) {
                i--;
                p = stk.pop();
            }
        }
        return ret.left;
    }
}