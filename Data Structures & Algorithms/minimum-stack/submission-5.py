class MinStack:

    def __init__(self):
        self.stack = []
        self.lowest = 0
        self.reps = {0:0}
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        cur = len(self.stack) - 1
        if val >= self.stack[self.lowest]:
            self.reps[cur] = self.lowest
        else:
            self.lowest = cur
            self.reps[cur] = cur

    def pop(self) -> None:
        del self.stack[-1]
        cur = len(self.stack) - 1
        if cur == -1:
            self.lowest = 0
        else:
            self.lowest = self.reps[len(self.stack) - 1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack[self.lowest]
        
