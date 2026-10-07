class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] * (amount + 1)
        for i in range(1, len(dp)):
            min_coins = 2 ** 31
            for coin in coins:
                if i - coin >= 0:
                    min_coins = min(dp[i - coin], min_coins)
            dp[i] = min_coins + 1
        if dp[-1] > 2 ** 31:
            return -1

        return dp[-1]

