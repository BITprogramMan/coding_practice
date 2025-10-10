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
    def process(self, s):

        def add_num(queue, num):
            if queue and queue[-1] != '+' and queue[-1] != '-':
                operator = queue.pop()
                val = queue.pop()
                num = (val * num) if operator == '*' else val / num
            queue.append(num)

        def get_num(queue):
            res = 0
            add = True
            while queue:
                curr = queue.pop()
                if curr == '+':
                    add = True
                elif curr == '-':
                    add = False
                else:
                    res += curr if add else -curr
            return res
        
        def value(s, i):
            pre = 0
            queue = []
            while i < len(s) and s[i] != ')':
                if s[i] >= '0' and s[i] <= '9':
                    pre = pre * 10 + int(s[i])
                elif s[i] != '(':
                    add_num(queue, pre)
                    queue.append(s[i])
                    pre = 0
                else:
                    pre, i = value(s, i + 1)
                i += 1
            add_num(queue, pre)
            val = get_num(queue)
            return val, i
        return value(s, 0)[0]



