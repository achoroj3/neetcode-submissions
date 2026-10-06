class Solution:

    def helper(self, cur_set, nums, subsets, i, seen):
        if tuple(cur_set) not in seen:
            subsets.append(cur_set)
            seen.add(tuple(cur_set))
        if i < len(nums):
            self.helper(cur_set, nums, subsets, i + 1, seen)
            self.helper(cur_set + [nums[i]], nums, subsets, i + 1, seen)
            
        
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        self.helper([] , nums, subsets, 0, set())
        return subsets