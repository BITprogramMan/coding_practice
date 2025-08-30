class minStack:
    """
实现一个特殊的栈，在实现栈的基本功能的基础上，再实现返回栈中最小元素
的操作。
要求：1.pop、push、getMin操作的时间复杂度都是O(1)；2.设计的栈类型可以
使用现成的栈结构
    """
    def __init__(self) -> None:
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self):
        if not self.stack:
            return None
        self.min_stack.pop()
        return self.stack.pop()
    
    def get_min(self):
        return self.min_stack[-1]
        

    
