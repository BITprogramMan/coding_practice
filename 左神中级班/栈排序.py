class Solution:
    """
    请编写一个程序，对一个栈里的整型数据，按升序进行排序（即排序前，栈里
    的数据是无序的，排序后最大元素位于栈顶），要求最多只能使用一个额外的
    栈存放临时数据，但不得将元素复制到别的数据结构中。
    """
    def process(self, stack):
        help = []
        while stack:
            if not help:
                help.append(stack.pop())
            elif help[-1] >= stack[-1]:
                help.append(stack.pop())
            else:
                val = stack.pop()
                while help and help[-1] < val:
                    stack.append(help.pop())
                help.append(val)
        while help:
            stack.append(help.pop())
