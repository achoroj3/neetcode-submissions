class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        aset = set()
        longest = 0
        #now we have 0(1) lookups
        for elem in nums:
            aset.add(elem)
        for elem in nums:
            if elem - 1 not in aset:
                current = 1
                next_elem = elem + 1
                while (next_elem in aset):
                    current+=1
                    next_elem+=1
                longest = max(longest, current)
        return longest
        