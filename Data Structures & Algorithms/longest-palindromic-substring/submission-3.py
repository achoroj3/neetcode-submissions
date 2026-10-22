class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        if not s:
            return ""
        longest_l = 0
        longest_r = 0

        for i in range(len(s) - 1):
            indexes = [[i, i], [i, i+1]]
            for l, r in indexes:
                if s[l] == s[r]:
                    while(0 < l and r < len(s) - 1 
                    and s[l - 1] == s[r + 1]):
                        l, r = l - 1, r + 1
                    if r - l > longest_r - longest_l:
                        longest_l, longest_r = l, r
        return s[longest_l:longest_r + 1]
            