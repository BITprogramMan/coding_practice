class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        count_dict = dict(Counter(magazine))
        for char in ransomNote:
            if count_dict.get(char, 0) == 0:
                return False
            else:
                count_dict[char] -= 1
        return True

        



