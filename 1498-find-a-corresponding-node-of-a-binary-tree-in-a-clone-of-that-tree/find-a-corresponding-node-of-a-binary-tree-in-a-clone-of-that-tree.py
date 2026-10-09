# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        stack = [(original, cloned)]
        while stack:
            tmp = stack.pop()
            if tmp[0] == target:
                return tmp[1]
            if tmp[0].left:
                stack.append((tmp[0].left, tmp[1].left))
            if tmp[0].right:
                stack.append((tmp[0].right, tmp[1].right))