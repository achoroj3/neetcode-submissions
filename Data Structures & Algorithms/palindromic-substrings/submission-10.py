class Solution:
    def extend(self, s, l ,r) -> int:
        ret = 0
        orig_l, orig_r = l, r
        while (l >= 0 and r < len(s) and s[l] == s[r]):
                ret+= 1
                l-=1
                r+=1
        l, r = orig_l, orig_r + 1

        while (l >= 0 and r < len(s) and s[l] == s[r]):
                ret+= 1
                l-=1
                r+=1
        return ret

    def countSubstrings(self, s: str) -> int:
        total = 0
        for i in range(len(s)):
            p = 0
            p = p + self.extend(s, i ,i)
            total += p
        return total
            #even check

