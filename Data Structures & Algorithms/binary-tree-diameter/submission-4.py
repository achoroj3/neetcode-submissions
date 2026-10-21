# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def helper(self, root, diameter):
        if not root:
            return 0
        l,r = 0, 0
        if root.left:
            l = 1 + self.helper(root.left, diameter)
        if root.right:
            r = 1 + self.helper(root.right, diameter)
        diameter[0] = max(diameter[0], l + r)
        return max(l, r)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = [0]
        self.helper(root, diameter)
        return diameter[0]
        