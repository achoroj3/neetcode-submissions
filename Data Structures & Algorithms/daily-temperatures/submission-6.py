class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        rlist = []
        stack = [] # temp, warmday
        for elem in reversed(temperatures):
            n = 0
            while stack and stack[-1][0] <= elem:
                n += stack.pop()[1]
            if len(stack) == 0:
                n = 0
                stack.append((elem, 0))
            else:
                n+=1
                stack.append((elem, n))
            rlist.append(n)
        rlist.reverse()
        return rlist
            

