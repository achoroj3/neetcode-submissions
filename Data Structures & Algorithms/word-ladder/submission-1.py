class Solution:
    def create_graph(self, beginWord: str, endWord: str, wordList: List[str]) -> dict:
        v = set([beginWord] + wordList)
        adj_list = {s:[] for s in v}
        m = len(beginWord)
        for node in v:
            transformations = []
            for i in range(m):
                for j in range(26):
                    n_c = chr(j + ord('a'))
                    if n_c != node[i]:
                        transformations.append(node[:i] + n_c + node[i+1:])
            for t in transformations:
                if t in v:
                    adj_list[node].append(t)
        return adj_list

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adj_list = self.create_graph(beginWord, endWord, wordList)
        path = deque([beginWord])
        ans = 1
        seen = set(beginWord)
        while path:
            len_path = len(path)
            for i in range(len_path):
                word = path.popleft()
                if (word == endWord):
                    return ans
                for nei in adj_list[word]:
                    if nei not in seen:
                        path.append(nei)
                        seen.add(nei)
            ans+= 1
        return 0 
