# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        root = set()
        child = set()
        val = {}
        for i, j, k in descriptions:
            child.add(j)
            if j in root:
                root.remove(j)
            if i not in child:
                root.add(i)
            if i in val and j in val:
                if k == 1:
                    val[i].left = val[j]
                else:
                    val[i].right = val[j]
            elif i in val:
                n = TreeNode(j)
                val[j] = n
                if k == 1:
                    val[i].left = n
                else:
                    val[i].right = n
            elif j in val:
                n = TreeNode(i)
                val[i] = n
                if k == 1:
                    n.left = val[j]
                else:
                    n.right = val[j]
            else:
                p = TreeNode(i)
                val[i] = p
                c = TreeNode(j)
                val[j] = c
                if k == 1:
                    p.left = c
                else:
                    p.right = c
        return val[next(iter(root))]