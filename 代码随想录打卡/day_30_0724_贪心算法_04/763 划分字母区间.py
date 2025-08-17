from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = [0] *26
        n = len(s)
        for i in range(n):
            last[ord(s[i]) - ord('a')] = i
        partition = []
        start = 0
        mostRight = 0
        for i in range(n):
            mostRight = max(mostRight, last[ord(s[i]) - ord('a')])
            if i == mostRight:
                partition.append(i - start + 1)
                start = i + 1
        return partition

