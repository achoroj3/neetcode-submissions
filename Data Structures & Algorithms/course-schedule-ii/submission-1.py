class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = {x:[] for x in range(numCourses)}
        indegree = [0] * numCourses
        for p in prerequisites:
            adj_list[p[1]].append(p[0]) # b -> a
            indegree[p[0]]+=1
        q = deque()
        for i, degree in enumerate(indegree):
            if degree == 0:
                q.append(i)
        if not q:
            return []
        seen = list(q)
        while (q):
            u = q.popleft()
            for v in adj_list[u]:
                indegree[v]-=1
                if indegree[v] == 0:
                    q.append(v)
                    seen.append(v)
        
        return seen if len(seen) == numCourses else []
        
        
            