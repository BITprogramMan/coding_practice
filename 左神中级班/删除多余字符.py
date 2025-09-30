class Solution:
    """
    给定一个全是小写字母的字符串str，删除多余字符，使得每种字符只保留一个，并让
    最终结果字符串的字典序最小
    【举例】
    str = "acbc"，删掉第一个'c'，得到"abc"，是所有结果字符串中字典序最小的。
    str = "dbcacbca"，删掉第一个'b'、第一个'c'、第二个'c'、第二个'a'，得到"dabc"，
    是所有结 果字符串中字典序最小的。
    """
    def process(self, s):
        count = [0] * 26
        for ch in s:
            count[ord(ch) - ord('a')] += 1
        result = []
        L = 0
        for R, ch in enumerate(s[L:]):
            idx = ord(ch) - ord('a')
            if count[idx] == -1:
                continue
            count[idx] -= 1
            if count[idx] > 0:
                continue
            pick = min([i for i in range(L, L + R + 1) if count[ord(s[i]) - ord('a')] != -1], key=lambda x: s[x])
            picked_char = s[pick]
            result.append(picked_char)
            count[ord(picked_char) - ord('a')] = -1

            for i in range(pick + 1, L + R + 1):
                char_dx = ord(s[i]) - ord('a')
                if count[char_dx] != -1:
                    count[char_dx] += 1
            L = pick + 1
        return ''.join(result)
    
if __name__ == '__main__':
    solution = Solution()
    res = solution.process("bbccacbab")
    print(res)




