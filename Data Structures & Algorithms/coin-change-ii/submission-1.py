class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        a = amount
        c = len(coins)
        dp = [[0 for _ in range(a + 1)] for _ in range(c)]

        i = 0
        while i < a + 1:
            dp[0][i] = 1
            i += coins[0]
        for i in range(c):
            dp[i][0] = 1
            
        for i in range(1, c):
            for j in range(1, a + 1):
                if j - coins[i] >= 0:
                    dp[i][j] += dp[i][j - coins[i]]
                dp[i][j] += dp[i - 1][j]
        return dp[-1][-1]