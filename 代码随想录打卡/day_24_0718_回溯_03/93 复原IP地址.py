from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        def backtrack(index, path, count, s, n):
            if index == n:
                if count == 4:
                    res.append('.'.join(path))
                return 
            if count >= 4:
                return 
            if s[index] == '0':
                path.append(s[index])
                count += 1
                backtrack(index + 1, path, count, s, n)
                path.pop()
            else:
                for i in range(index, min(index + 3, n)):
                    if int(s[index:i + 1]) > 255:
                        break
                    path.append(s[index:i + 1])
                    count += 1
                    backtrack(i + 1, path, count, s, n)
                    path.pop()
                    count -= 1
        backtrack(0, [], 0, s, len(s))
        return res

                
if __name__ == '__main__':
    solution = Solution()
    s = "0000"
    res = solution.restoreIpAddresses(s)
    print(res)
