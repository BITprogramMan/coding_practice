def ReverseStackUsingRecursive(stack):
    def dfs(stack):
        if len(stack) == 1:
            return stack.pop()
        else:
            top = stack.pop()
            res = dfs(stack)
            stack.append(top)
            return res
        
    if len(stack) < 2:
        return stack
    bottom = dfs(stack)
    ReverseStackUsingRecursive(stack)
    stack.append(bottom)

if __name__ == '__main__':
    stack = [1, 2, 3, 4]
    ReverseStackUsingRecursive(stack)
    print(stack)


