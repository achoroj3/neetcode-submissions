class Solution:

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(point) -> double:
            return math.sqrt(point[0] ** 2 + point[1] ** 2)
        pq = []
        for elem in points:
            heapq.heappush(pq, (distance(elem), elem))
        closest = []
        while(k > 0):
            closest.append(heapq.heappop(pq)[1])
            k-=1
        return closest
        