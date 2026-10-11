"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        node_copy = {1 : Node(node.val, None)}
        visit = [node]
        edges = set()
        while (len(visit) > 0):
            cur = visit.pop()
            for neighbor in cur.neighbors:
                if ((cur.val, neighbor.val) not in edges and 
                (neighbor.val, cur.val) not in edges):
                    node_copy[neighbor.val] = Node(neighbor.val, None)
                    visit.append(neighbor)
                    edges.add((cur.val, neighbor.val))
        for edge in edges:
            node_A = node_copy[edge[0]]
            node_B = node_copy[edge[1]]
            node_A.neighbors.append(node_B)
            node_B.neighbors.append(node_A)
        return node_copy[1]
        


   
 
