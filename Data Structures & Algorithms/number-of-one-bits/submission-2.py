class Solution:
    def hammingWeight(self, n: int) -> int:

        masks = [2 ** i for i in range(32)]
        count = 0
        for mask in masks:
            if mask & n > 0:
                count+=1
        return count

        # 10
        # 100
        # 1000
        # 10000
 