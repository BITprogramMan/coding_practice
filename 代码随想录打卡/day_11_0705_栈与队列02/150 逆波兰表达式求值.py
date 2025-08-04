from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == '+':
                v1 = stack.pop()
                v2 = stack.pop()
                token = v2 + v1
                stack.append(token)
            elif token == '-':
                v1 = stack.pop()
                v2 = stack.pop()
                token = v2 - v1
                stack.append(token)  
            elif token == '*':
                v1 = stack.pop()
                v2 = stack.pop()
                token = v2 * v1
                stack.append(token)  
            elif token == '/':
                v1 = stack.pop()
                v2 = stack.pop()
                token = v2 // v1 if v2 * v1 >= 0 else - (abs(v2) // abs(v1) )
                stack.append(token)  
            else:
                stack.append(int(token))
        return stack.pop()
    

if __name__ =='__main__':
    solution = Solution()
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    res = solution.evalRPN(tokens)
    print(res)

