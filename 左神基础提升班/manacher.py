class Solution:
    def process(self, s):
        s1 = '#' + '#'.join(list(s)) + '#'
        n = len(s1)
        huiWenRadiusList = [0] * n
        mostRight = -1
        c = -1
        res_start, res = -1, -1
        for i in range(n):
            if mostRight > i:
                huiWenRadiusList[i] = min(mostRight - i, huiWenRadiusList[2 * c - i])
            else:
                huiWenRadiusList[i] = 1
            while i + huiWenRadiusList[i] < n and i - huiWenRadiusList[i] > -1:
                if s1[i + huiWenRadiusList[i]] == s1[i - huiWenRadiusList[i]]:
                    huiWenRadiusList[i] += 1
                else:
                    break
            if i + huiWenRadiusList[i] > mostRight:
                mostRight = i + huiWenRadiusList[i]
                c = i
            if huiWenRadiusList[i] > res:
                res = huiWenRadiusList[i]
                res_start = i
        if res_start & 1 == 1:
            res_start = max(0, (res_start - 1) // 2 - (res - 1) // 2)
        else:
            res_start = max(0, res_start // 2 - (res - 1) // 2)
        return s[res_start: res_start + res - 1]
                
if __name__ == '__main__':
    solutin = Solution()
    res = solutin.process('fdbbdk')
    print(res)


