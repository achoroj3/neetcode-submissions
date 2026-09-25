class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp[i] = max amount of money you can rob without alerting police at house i
        # you either rob this house (and therefore cannot rob the previous)
        # so dp[i] = nums[i] + dp[i-2]
        # or you leave this house dp[i] = dp[i-1]

        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        n = len(nums)
        dp = [0] * n
        dp[0], dp[1] = nums[0], max(nums[0],nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        return dp[n - 1]

