class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        if not s:
            return ""
        longest = s[0]
        for i in range(len(s) - 1):
            indexes = [[i, i], [i, i+1]]
            for l, r in indexes:
                if s[l] == s[r]:
                    while(0 < l and r < len(s) - 1 
                    and s[l - 1] == s[r + 1]):
                        l, r = l - 1, r + 1
                    longest = s[l:r+1] if r - l + 1 > len(longest) else longest
        return longest
            