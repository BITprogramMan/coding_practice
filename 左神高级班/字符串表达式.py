class Solution:
    """
    给定一个字符串str，str表示一个公式，公式里可能有整数、加减乘除符号和左右
    括号，返回公式的计算结果。
    【举例】
    str="48*((70-65)-43)+8*1"，返回-1816。
    str="3+1*4"，返回7。
    str="3+(1*4)"，返回7。
    【说明】
    1．可以认为给定的字符串一定是正确的公式，即不需要对str做公式有效性检查。
    2．如果是负数，就需要用括号括起来，比如"4*(-3)"。但如果负数作为公式的开头
    或括号部分的开头，则可以没有括号，比如"-3*4"和"(-3*4)"都是合法的。
    3．不用考虑计算过程中会发生溢出的情况。
    """
    def getValue(self, s):
        def addNum(queue, num):
            if queue:
                cur = 0
                top = queue.pop()
                if top == '+' or top == '-':
                    queue.append(top)
                else:
                    cur = queue.pop()
                    num = cur * num if top == '*' else cur / num
            queue.append(num)
        
        def getNum(queue):
            res = 0
            add = True
            cur = None
            num = 0
            while queue:
                cur = queue.pop()
                if cur == '+':
                    add = True
                elif cur == '-':
                    add = False
                else:
                    num = float(cur)
                    res += (num if add else -num)
            return res
        
        def value(s, i):
            queue = []
            pre = 0
            bra = None
            while i < len(s) and s[i] != ')':
                if s[i] >= '0' and s[i] <= '9':
                    pre = pre * 10 + ord(s[i]) - ord('0')
                elif s[i] != '(':
                    addNum(queue, pre)    
                    queue.append(s[i])
                    i += 1
                else:
                    bra = value(s, i + 1)
                    pre = bra[0]
                    i = bra[1] + 1
            addNum(queue, pre)
            return getNum(queue), i
        
        return value(s, 0)[0]