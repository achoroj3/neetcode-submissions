class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # max amt any two bars can store = distance * min(leftbar, rightbar)
        left = 0
        right = len(heights) - 1
        max_amt = 0
        while (left < right):
            max_amt = max((right - left) * min(heights[left], heights[right]), max_amt)
            if heights[left] < heights[right]:
                left+=1
            else:
                right-=1
        return max_amt

        