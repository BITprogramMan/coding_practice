from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        digit_mapping = {'2': ['a', 'b', 'c'],
                         '3': ['d','e', 'f'],
                         '4': ['g', 'h', 'i'],
                         '5': ['j', 'k', 'l'],
                         '6': ['m', 'n', 'o'],
                         '7': ['p', 'q', 'r', 's'],
                         '8': ['t', 'u', 'v'],
                         '9': ['w', 'x', 'y', 'z']}
        res = []
        def backtrack(index, path, digits, length):
            if index == length:
                res.append(path)
                return
            for char in digit_mapping[digits[index]]:
                path = path + char
                backtrack(index + 1, path, digits, length)
                path = path[:-1]

        backtrack(0, '', digits, len(digits))
        return res
    
if __name__ == '__main__':
    solution = Solution()
    digits = '23'
    res = solution.letterCombinations(digits)
    print(res)
            
