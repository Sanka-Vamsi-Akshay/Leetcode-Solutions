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
    public int height(TreeNode root){
        if(root == null){
            return 0;
        }else{
            root.val = 1 + Math.max(height(root.left), height(root.right));
            return root.val;
        }
    }
    public boolean balanceCheck(TreeNode root){
        if(root == null){
            return true;
        }
        int tmp = ((root.left != null) ? root.left.val : 0) - ((root.right != null) ? root.right.val : 0);
        return tmp >= -1 && tmp <= 1 && balanceCheck(root.left) && balanceCheck(root.right);
    }
    public boolean isBalanced(TreeNode root) {
        if(root == null){
            return true;
        }
        height(root);
        return balanceCheck(root);
    }
}