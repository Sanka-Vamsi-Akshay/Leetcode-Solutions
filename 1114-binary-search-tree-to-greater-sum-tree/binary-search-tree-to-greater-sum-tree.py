# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        return self.inorder(root.left) + [root.val] + self.inorder(root.right)
    def change(self, root: Optional[TreeNode]) -> None:
        if root is None:
            return
        root.val = self.val[root.val]
        self.change(root.left)
        self.change(root.right)
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        arr = self.inorder(root)
        tot = 0
        self.val = {}
        for i in range(len(arr) - 1, -1, -1):
            tot += arr[i]
            self.val[arr[i]] = tot
        self.change(root)
        return root