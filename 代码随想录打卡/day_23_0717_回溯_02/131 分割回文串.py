from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def backtrackv0(index, path, s, n):
            if index == n:
                if path[-1] == path[-1][::-1]:
                    res.append(path[:])
                return 
            if len(path) > 0:
                if path[-1] == path[-1][::-1]:
                    path.append(s[index])
                    backtrack(index + 1, path, s, n)
                    path.pop()
                path[-1] += s[index]
                backtrack(index + 1, path, s, n)
                path[-1] = path[-1][:-1]
            else:
                path.append(s[index])
                backtrack(index + 1, path, s, n)
                path.pop()

        # backtrackv0(0, [], s, len(s))
        # return res

        def backtrack(index, path, s, n):
            if index == n:
                res.append(path[:])
                return
            for i in range(index, n):
                if s[index: i + 1] == s[index: i + 1][::-1]:
                    path.append(s[index: i + 1])
                    backtrack(i + 1, path, s, n)
                    path.pop()
        backtrack(0, [], s, len(s))
        return res



if __name__ == '__main__':
    solution = Solution()
    s = 'aab'
    res = solution.partition(s)
    print(res)
