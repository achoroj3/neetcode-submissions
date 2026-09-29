class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        target = int(sum(nums) / 2)
        path = [(nums[0], 0)]
        seen = set()

        while (len(path) > 0):
            elem = path.pop()
            t = (elem[0], elem[1])
            if t in seen:
                continue
            else:
                seen.add(t)
            if elem[0] == target:
                return True
            index = elem[1] + 1
            if index < len(nums):
                if (elem[0] + nums[index] <= target):
                    path.append([elem[0] + nums[index], index])
                path.append([elem[0], index])
        return False