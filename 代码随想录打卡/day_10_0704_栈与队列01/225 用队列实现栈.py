class MyStack:

    def __init__(self):
        self.stack = []
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        
    def pop(self) -> int:
        if not self.stack:
            return None
        for _ in range(len(self.stack) - 1):
            self.stack.append(self.stack.pop(0))
        return self.stack.pop(0)

    def top(self) -> int:
        ans = self.pop()
        self.push(ans)
        return ans
        

    def empty(self) -> bool:
        if not self.stack:
            return True
        return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()