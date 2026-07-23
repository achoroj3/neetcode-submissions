# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    #depth finding logic
    def depth(self, root:TreeNode, node:TreeNode) -> int:
        if root.val == node.val:
            return 0
        if node.val < root.val:
            return 1 + self.depth(root.left, node)
        else:
            return 1 + self.depth(root.right, node)
        #-------
    #ancestor finding logic
    def isAncestor(self, root:TreeNode, node: TreeNode) -> bool:
        if root is None:
            return False
        if root.val == node.val:
            return True
        return self.isAncestor(root.left, node) or self.isAncestor(root.right, node)

    def findAncestors(self, root: TreeNode, p: TreeNode, q: TreeNode, ancestor_list: List[int]):
        if root is None:
            return
        if self.isAncestor(root, p) and self.isAncestor(root, q):
            ancestor_list.append(root)
        self.findAncestors(root.left, p, q, ancestor_list)
        self.findAncestors(root.right, p, q, ancestor_list)
    #----------------------
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #create a function that finds all ancestors
        #then find the lowest one.
        ancestor_list = []
        self.findAncestors(root, p, q, ancestor_list)
        lowest_ancestor = root
        depth = 0
        
        for ancestor in ancestor_list:
            print("node:", ancestor.val, "current lowest:", lowest_ancestor.val)
            new_depth = self.depth(root, ancestor)
            print ("new_depth:", new_depth)
            if new_depth > depth:
                depth = new_depth
                lowest_ancestor = ancestor
        return lowest_ancestor

            
        
        

