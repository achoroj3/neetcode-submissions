class Solution:
    def hammingWeight(self, n: int) -> int:
        i = 0
        while (2 ** i) <= n:
            i+=1
        i-=1
        count = 0
        while (n > 0):
            if (n - (2 ** i) >= 0):
                count+=1
                n-=(2 ** i)
            i-=1
        return count