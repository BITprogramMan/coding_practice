from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if s in wordDict or s == '':
            return True
        for word in wordDict:
            word_len = len(word)
            if s[:word_len] == word and self.wordBreak(s[word_len:], wordDict):
                return True
        return False

    def wordBreakv1(self, s: str, wordDict: List[str]) -> bool:
        def recursive(s, wordDict, dp):
            if s in wordDict or s == '':
                return True
            if s in dp:
                return dp[s]
            for word in wordDict:
                word_len = len(word)
                if s[:word_len] == word and recursive(s[word_len:], wordDict, dp):
                    dp[s] = True
                    return dp[s]
            dp[s] = False
            return dp[s]
        dp = {}
        return recursive(s, wordDict, dp)
    
    def wordBreakv2(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        wordDict.sort(key=lambda x: len(x))
        for i in range(1, n + 1):
            for word in wordDict:
                if len(word) > i:
                    break
                if s[i - len(word):i] == word and dp[i - len(word)]:
                    dp[i] = True
                    break
        return dp[-1]

