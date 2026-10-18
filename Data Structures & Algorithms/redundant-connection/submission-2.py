class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj_list = [[] for _ in range(n + 1)]
        degrees = [0] * (n + 1)
        d = deque()

        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
            degrees[u] += 1
            degrees[v] += 1
        for i in range(1, n + 1):
            if degrees[i] == 1:
                d.append(i)
        while d:
            to_prune = d.popleft()
            degrees[to_prune] = 0

            for v in adj_list[to_prune]:
                if degrees[v] > 0:
                    degrees[v] -= 1
                    if degrees[v] == 1:
                        d.append(v)
        for u, v in reversed(edges):
            if degrees[u] > 0 and degrees[v] > 0:
                return [u, v] 
        return []
