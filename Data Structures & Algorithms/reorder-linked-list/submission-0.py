# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        cur = head
        length = 0
        while (cur):
            length+=1
            cur = cur.next
        half = length//2

        cur = head
        while (half > 0):
            half-=1
            cur = cur.next
        other_list_head = cur.next
        cur.next = None
        #reverse a linked list from other_list_head
        p = None
        c = other_list_head

        while (c):
            n = c.next
            c.next = p
            p = c
            c = n
        #combine lists
        first, second = head, p
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first,second = tmp1, tmp2

        





        
