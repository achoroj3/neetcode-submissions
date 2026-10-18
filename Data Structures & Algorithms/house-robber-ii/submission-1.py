class Solution:
    def rob(self, nums: List[int]) -> int:
        ret = 0
        if len(nums) == 0:
            return ret
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        arr1 = nums[1:]
        arr2 = nums[:-1]
        dp = [arr1[0], max(arr1[0], arr1[1])]
        for i in range(2, len(arr1)):
            dp.append(max(dp[i-2] + arr1[i], dp[i-1]))
        ret = dp[-1]
        dp = [arr2[0], max(arr2[0], arr2[1])]
        for i in range(2, len(arr2)):
            dp.append(max(dp[i-2] + arr2[i], dp[i-1]))
        
        return max(dp[-1], ret)