import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = stones[:]
        heapq.heapify_max(pq)
        while len(pq) > 1:
            y = heapq.heappop_max(pq)
            x = heapq.heappop_max(pq)
            print(x, y)
            if x < y:
                heapq.heappush_max(pq, y - x)
        if len(pq) == 0:
            return 0
        return heapq.heappop_max(pq)