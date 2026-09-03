# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #process everything in level order, right to left
        #when the level has been pushed, the top element is the right side view
        #then pop the rest of the level, and continue until null
        if not root:
            return []
        d = deque([root])
        l_size = 0
        values = []
        while (d):
            l_size = len(d)
            values.append(d[-1].val)
            for i in range(l_size):
                if d[-1].right:
                    d.appendleft(d[-1].right)
                if d[-1].left:
                    d.appendleft(d[-1].left)
                del d[-1]
        return values

            