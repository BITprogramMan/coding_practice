class Solution:
    def isHappyv1(self, n: int) -> bool:
        def caluate(n):
            nums = list(map(int, list(str(n))))
            ans = sum([i ** 2 for i in nums])
            return ans
        visited = set()
        while True:
            res = caluate(n)
            if res == 1:
                return True
            else:
                if res in visited:
                    return False
                else:
                    visited.add(res)
                    n = res


    def isHappy(self, n: int) -> bool:
        def caluate(n):
            ans = 0
            while n:
                n, r = divmod(n, 10)
                ans += r ** 2
            return ans
        visited = set()
        while True:
            n = caluate(n)
            if n == 1:
                return True
            else:
                if n in visited:
                    return False
                else:
                    visited.add(n)



if __name__ == '__main__':
    solution = Solution()
    n = 19
    res = solution.isHappy(n)
    print(res)