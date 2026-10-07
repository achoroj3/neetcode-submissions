class Solution:

    def helper(self, nums, target, combinations, cur, i):
        if i >= len(nums):
            return
        total = sum(cur)
        if total == target:
            combinations.append(cur)
        if total < target:
            self.helper(nums, target, combinations, cur.copy(), i + 1)
            cur.append(nums[i])
            self.helper(nums, target, combinations, cur.copy(), i)



        
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combinations = []
        self.helper(nums, target, combinations, [], 0)
        return combinations