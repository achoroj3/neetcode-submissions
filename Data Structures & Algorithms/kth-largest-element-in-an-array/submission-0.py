class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #min heap
        pq = []
        for num in nums:
            heapq.heappush(pq, num)
            if len(pq) > k:
                heapq.heappop(pq)
        return heapq.heappop(pq)
