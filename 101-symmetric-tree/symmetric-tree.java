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
    public boolean compare(TreeNode lRoot, TreeNode rRoot){
        if(lRoot == null && rRoot == null){
            return true;
        }else if(lRoot == null || rRoot == null){
            return false;
        }else{
            return lRoot.val == rRoot.val && compare(lRoot.left, rRoot.right) && compare(lRoot.right, rRoot.left);
        }
    }
    public boolean isSymmetric(TreeNode root) {
        return compare(root.left, root.right);
    }
}