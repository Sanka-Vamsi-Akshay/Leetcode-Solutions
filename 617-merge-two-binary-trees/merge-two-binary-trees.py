# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeVal(self, root1: Optional[TreeNode], root2: Optional[TreeNode]):
        if root1.left and root2.left:
            root1.left.val += root2.left.val
            self.mergeVal(root1.left, root2.left)
        elif root2.left:
            root1.left = root2.left
        if root1.right and root2.right:
            root1.right.val += root2.right.val
            self.mergeVal(root1.right, root2.right)
        elif root2.right:
            root1.right = root2.right
        
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 and root2:
            root1.val += root2.val
            self.mergeVal(root1, root2)
            return root1
        elif root1:
            return root1
        elif root2:
            return root2