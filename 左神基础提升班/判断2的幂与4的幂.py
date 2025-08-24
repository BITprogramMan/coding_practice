class Solution:
    def is2Power(self, n):
        return n & (n - 1) == 0
    
    def is4Power(self, n):
        return (n & (n - 1)) == 0 and (n & 0xaaaaaaaa) == 0


if __name__ == '__main__':
    solution = Solution()
    n = 16
    print(solution.is2Power(n))
