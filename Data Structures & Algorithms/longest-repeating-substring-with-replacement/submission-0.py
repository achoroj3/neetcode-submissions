class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        for i in range(26):
            count[chr(i + 65)] = 0
        
        l= 0
        res = 0
        for r in range(len(s)):
            count[s[r]]+= 1
            while(((r-l+1) - max(count.values()) > k)):
                count[s[l]]-=1
                l+=1
            res = max(res, r - l + 1)
        return res

