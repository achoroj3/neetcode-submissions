class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        seen = set()
        st = [0]
        while st:
            start = st.pop()
            if start in seen:
                continue
            seen.add(start)
            for word in wordDict:
                if s.startswith(word, start):
                    if start + len(word) == len(s):
                        return True
                    st.append(start + len(word))
                       
        return False



