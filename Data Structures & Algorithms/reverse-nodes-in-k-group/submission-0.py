# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseGroup(self, start) -> List[ListNode]:
        cur = start.next
        tail = start
        p = start
        p.next = None
        while (cur):
            temp = cur.next
            cur.next = p
            p = cur
            cur = temp
        return [p, tail]
            
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur = dummy = ListNode(0, head)
        start = end = head
        flag = True
        while(end):
            for i in range(k - 1):
                end = end.next
                if not end:
                    cur.next = nextGroupNode
                    return dummy.next
            nextGroupNode = end.next
            end.next = None
            group = self.reverseGroup(start)
            cur.next = group[0]
            cur = group[1]
            start = end = nextGroupNode
            


            
            
        return dummy.next

