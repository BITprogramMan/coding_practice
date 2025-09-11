class Solution:
    def intToRoman(self, num: int) -> str:
        c = [['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'],
             ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'],
             ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'],
             ['', 'M', 'MM', 'MMM']]
        res = []
        for i in range(3, -1, -1):
            res.append(c[i][num // (10 ** i) % 10])   # 获取每个十进制位上的数
        return ''.join(res)