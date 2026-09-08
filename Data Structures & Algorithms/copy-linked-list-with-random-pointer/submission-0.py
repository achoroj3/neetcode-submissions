"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        dummy = Node(0)
        cur = dummy
        cur2 = head
        #create copies
        while (cur2):
            cur.next = Node(cur2.val)
            cur = cur.next
            cur2 = cur2.next
        #create copies from original to new
        cur = dummy.next #head
        cur2 = head
        amap = {}
        while(cur):
            amap[cur2] = cur
            cur2 = cur2.next
            cur = cur.next
        #update randoms from existing copy mapping
        cur = dummy.next
        cur2 = head
        while(cur):
            if cur2.random is not None:
                cur.random = amap[cur2.random]
            cur = cur.next
            cur2 = cur2.next
        return dummy.next