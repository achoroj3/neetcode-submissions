# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next

# class Solution:
#     def isolateMin(self, lists, cur) -> ListNode: #isolate cur and return min node
#         minNode = ListNode(10001)
#         index = -1
#         for i in range(len(lists)):
#             if lists[i] and lists[i].val < minNode.val:
#                 minNode = lists[i]
#                 index = i
#         if index != -1:
#             lists[index] = lists[index].next
#             minNode.next = None
#             return minNode
#         else:
#             return None

#     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#         dummy = ListNode(0)
#         cur = dummy
#         done = False
#         numNodes = 0
#         for elem in lists:
#             ptr = elem
#             while(ptr):
#                 numNodes +=1
#                 ptr = ptr.next
#         while (numNodes > 0):
#             cur.next = self.isolateMin(lists, cur)
#             cur = cur.next
#             numNodes-= 1
#         return dummy.next
# The runtimes were misleading, and this version worked on leetcode. I will
# include the brute force method here as my submitted solution.

class Solution:
    def mergeKLists(self, lists):
        result = []

        for head in lists:
            while head:
                result.append(head.val)
                head = head.next

        result.sort()

        dummy = ListNode(0)
        current = dummy

        for value in result:
            current.next = ListNode(value)
            current = current.next

        return dummy.next