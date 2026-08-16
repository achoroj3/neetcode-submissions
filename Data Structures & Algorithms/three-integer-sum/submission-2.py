class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        return_set = set()
        nums.sort()
        for i in range(len(nums)):
            target = nums[i]
            l = 0
            r = len(nums) - 1
            
            while(l < r):
                if nums[l] + nums[r] == -target and (i != l and i != r):
                    triplet = tuple(sorted([nums[r], nums[l], target]))
                    if triplet not in return_set:
                        return_set.add(triplet)        
                if (nums[l] + nums[r] > -target or i == r):
                    r-=1
                elif (nums[l] + nums[r] <= -target or i == l):
                    l+=1
        return list(return_set)


