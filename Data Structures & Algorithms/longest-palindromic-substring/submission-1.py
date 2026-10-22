class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        if not s:
            return ""
        longest = s[0]
        for i in range(len(s) - 1):
            indexes = [[i, i], [i, i+1]]
            for l, r in indexes:
                while(0 < l and r < len(s) - 1 
                and s[l - 1] == s[r + 1]
                and s[l] == s[r]
                ):
                    l, r = l - 1, r + 1
                
                if s[l] == s[r]:
                    longest = s[l:r+1] if r - l + 1 > len(longest) else longest
        return longest
            