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
    
//     private TreeNode rec(int nums[], int i){
//         if(i==)
            
//         int mn=0 , mi
//     }
    
    public TreeNode constructMaximumBinaryTree(int[] nums) {
        
//         if(nums.length == 0) return null;
        
//         int mn = nums[0], mi=0;
//         for(int i=0;i<nums.length;i++){
//             if(nums[i]>mn){
//                 mn = nums[i];
//                 mi = i;
//             }
//         }
//         TreeNode root = new TreeNode(mn);
//         root.left = constructMaximumBinaryTree(Arrays.copyOfRange(nums,0,mi));
//         root.right = constructMaximumBinaryTree(Arrays.copyOfRange(nums,mi+1,nums.length));
//         return root;
        Deque<TreeNode> stack = new LinkedList<>();
        for(int i = 0; i < nums.length; i++) {
            TreeNode curr = new TreeNode(nums[i]);
            while(!stack.isEmpty() && stack.peek().val < nums[i]) {
                curr.left = stack.pop();
            }
            if(!stack.isEmpty()) {
                stack.peek().right = curr;
            }
            stack.push(curr);
        }
        
        return stack.isEmpty() ? null : stack.removeLast();
    }
}