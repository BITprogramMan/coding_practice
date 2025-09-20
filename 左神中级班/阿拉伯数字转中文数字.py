class Solution:
    def num1To9(self, num):
        if num < 1 or num > 9:
            raise ValueError
        names = ["一", "二", "三", "四", "五", "六", "七", "八", "九"]
        return names[num - 1]
    
    def num1To99(self, num, hasBai):
        if num < 1 or num > 99:
            raise ValueError
        if num < 10:
            return self.num1To9(num)
        shi = num // 10
        if shi == 1 and not hasBai:
            return '十' + self.num1To9(num % 10)
        else:
            return self.num1To9(shi) + '十' + self.num1To9(num % 10)
        
    def num1To999(self, num):
        if num < 1 or num > 999:
            raise ValueError
        if num < 100:
            return self.num1To99(num, False)
        res = self.num1To9(num // 100) + '百'
        rest = num % 100
        if rest == 0:
            return res
        elif rest >= 10:
            res += self.num1To99(rest, True)
        else:
            res += "零" + self.num1To9(rest)
        return res

    def num1To9999(self, num):
        if num < 1 or num > 9999:
            raise ValueError
        if num < 1000:
            return self.num1To999(num)
        res = self.num1To9(num // 1000) + "千"
        rest = num % 1000
        if rest == 0:
            return res
        elif num > 100:
            res += self.num1To999(rest)
        else:
            res += "零" + self.num1To99(rest, False)
        return res
    
    def num1To99999999(self, num):
        if num < 1 or num > 99999999:
            raise ValueError
        if num < 9999:
            return self.num1To9999(num)
        res = self.num1To9999(num // 10000) + "万"
        rest = num % 10000
        if rest == 0:
            return res
        else:
            if rest < 1000:
                return res + "零" + self.num1To999(rest)
            else:
                return res + self.num1To9999(rest)

    def getNumChiExp(self, num):
        if num == 0:
            return "零"
        res = '负' if num < 0 else ''
        num_yi = abs(num // 100000000)
        rest =  abs(num % 100000000)
        if num_yi == 0:
            return res + self.num1To99999999(rest)
        else:
            if rest < 10000000:
                return res + '零' + self.num1To99999999(rest)
            else:
                return res + self.num1To99999999(rest)

            



