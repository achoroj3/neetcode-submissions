class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # the question is what is the search principle

        l = 0
        r = len(nums) - 1
        m = (l + r) //2

        # maybe it has to do with the index and the number I'm looking at
        # one side is sorted and one side isnt maybe i can use it
        while (l <= r):
            m = (l + r) // 2
            if(nums[m] == target):
                return m
            if (nums[m] > target and nums[l] < nums[r]): # sorted range, right
                r = m - 1
            elif (nums[m] < target and nums[l] < nums[r]): # sorted range, left
                l = m + 1
            elif (nums[l] <= nums[m]):
                if(nums[l] <= target < nums[m]):
                    r = m - 1
                else:
                    l = m + 1
            elif (nums[r] >= nums[m]):
                if (nums[m] < target <= nums[r]):
                    l = m + 1
                else:
                    r = m - 1
        return -1