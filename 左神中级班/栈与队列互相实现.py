from collections import deque
class Solution:
    """
    如何仅用队列结构实现栈结构?
    如何仅用栈结构实现队列结构?
    """
    class stack2deque:
        def __init__(self) -> None:
            self.stack_in = []
            self.stack_out = []

        def push(self, val):
            self.stack_in.append(val)

        def pop(self):
            if self.stack_out:
                return self.stack_out.pop()
            else:
                while self.stack_in:
                    self.stack_out.append(self.stack_in.pop())
                if self.stack_out:
                    return self.stack_out.pop()
                else:
                    return None
        def peek(self):
            if not self.stack_out and not self.stack_in:
                return None
            elif not self.stack_out:
                while self.stack_in:
                    self.stack_out.append(self.stack_in.pop())
                    
            return self.stack_out[-1]
        
    class deque2stackv1:
        def __init__(self):
            self.queue = deque()
            self.help = deque()

        def push(self, val):
            self.queue.append(val)

        def swap(self):
            self.queue, self.help = self.help, self.queue

        def pop(self):
            if not self.queue:
                return None
            while len(self.queue) > 1:
                self.help.append(self.queue.popleft())
            res = self.queue.popleft()
            self.swap()
            return res
        
        def peek(self):
            if not self.queue:
                return None
            while len(self.queue) > 1:
                self.help.append(self.queue.popleft())
            res = self.queue.popleft()
            self.help.append(res)
            self.swap()
            return res  

    class deque2stackv2:
        def __init__(self):
            """使用单个队列实现栈"""
            self.queue = deque()
        
        def push(self, x: int) -> None:
            """将元素x压入栈顶"""
            # 获取当前队列大小
            size = len(self.queue)
            
            # 添加新元素
            self.queue.append(x)
            
            # 将前面的size个元素重新排列到新元素后面
            # 这样新元素就变成了队列的第一个元素
            for _ in range(size):
                self.queue.append(self.queue.popleft())

        def pop(self) -> int:
            """移除并返回栈顶元素"""
            if self.empty():
                raise IndexError("pop from empty stack")
            return self.queue.popleft()
        
        def top(self) -> int:
            """返回栈顶元素（不移除）"""
            if self.empty():
                raise IndexError("top from empty stack")
            return self.queue[0]
        
        def empty(self) -> bool:
            """检查栈是否为空"""
            return len(self.queue) == 0
        
        def __str__(self):
            """打印栈内容（用于调试）"""
            return f"Stack({list(self.queue)})"


