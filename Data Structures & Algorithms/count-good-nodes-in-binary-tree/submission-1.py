# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def helper(self, root, g) -> int:
        if not root:
            return 0
        dummy = 0
        if root.val >= g:
            g = root.val
            dummy = 1
        return dummy + self.helper(root.right, g) + self.helper(root.left, g)


    def goodNodes(self, root: TreeNode) -> int:
        return self.helper(root, root.val) 