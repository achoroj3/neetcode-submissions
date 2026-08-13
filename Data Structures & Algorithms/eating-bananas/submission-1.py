class Solution:
    def hoursNeeded(self, piles: List[int], k: int) -> int:
        total = 0
        for p in piles:
            total += (p + k - 1) // k  # ceil(p / k)
        return total

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        while low < high:
            mid = (low + high) // 2
            curh = self.hoursNeeded(piles, mid)
            if curh <= h:
                high = mid          # mid works, try smaller
            else:
                low = mid + 1       # mid too slow, need bigger
        return low