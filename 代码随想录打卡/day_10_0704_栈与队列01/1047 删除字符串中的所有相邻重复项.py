class Solution:
    def removeDuplicatesv1(self, s: str) -> str:
        stack = []
        for c in s:
            if not stack or stack[-1] != c:
                stack.append(c)
            else:
                stack.pop()
        return ''.join(stack)
    

    def removeDuplicates(self, s: str) -> str:
        res = list(s)
        slow  = 0
        for fast in range(len(s)):
            res[slow] = res[fast]
            if slow > 0 and res[slow] == res[slow - 1]:
                slow -= 1
            else:
                slow += 1
        return ''.join(res[:slow])
            
