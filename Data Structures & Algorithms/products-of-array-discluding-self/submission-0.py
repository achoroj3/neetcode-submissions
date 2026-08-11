class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        L = []
        R = []
        product = 1
        L.append(1)
        for i in range(1, len(nums)):
            product *= nums[i - 1]
            L.append(product)
        product = 1
        R.append(1)
        for i in range(len(nums) - 2, -1, -1):
            product *= nums[i + 1]
            R.append(product)
        R.reverse()
        print(len(L), len(R))
        return_list = []
        for i in range(len(nums)):
            return_list.append(L[i] * R[i])
        return return_list
            
        
