class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        #map indicies to l and r in O(n) time
        m = height[0]
        leftMax = []
        rightMax = []
        for i in range(len(height)):
            m = max(m, height[i])
            leftMax.append(m)
        m = height[len(height) - 1]
        for i in range(len(height) - 1, -1, -1):
            m = max(m, height[i])
            rightMax.append(m)
        rightMax.reverse()
        for i in range(len(height)):
            total += min(leftMax[i], rightMax[i]) - height[i]
        return total