class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = {x:[] for x in range(n)}
        seen = set()
        components = 0

        for edge in edges:
            u, v = edge
            adj_list[u].append(v)
            adj_list[v].append(u)
        for i in range(n):
            path = [i]
            if i not in seen:
                while path:
                    node = path.pop()
                    for nei in adj_list[node]: # Iterate through neighboring nodes.
                        if nei not in seen:
                            path.append(nei)
                            seen.add(nei)
                components+=1
        return components
