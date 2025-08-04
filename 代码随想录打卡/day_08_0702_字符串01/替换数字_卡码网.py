class Solution(object):
    def subsitute_numbers(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        count_digit = 0
        for i in range(n):
            if s[i].isdigit():
                count_digit += 1
        res = [0] * n + [0] * 5 * count_digit
        idx = len(res) - 1
        for i in range(n-1, -1, -1):
            if s[i].isdigit():
                res[idx - 5:idx + 1] = list('number')
                idx -= 6
            else:
                res[idx] = s[i]
                idx -= 1
        return ''.join(res)
    
if __name__ == '__main__':
    solution = Solution()
    s = 'a2b'
    res = solution.subsitute_numbers(s)
    print(res)



        