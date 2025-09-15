class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        elif n == 2 or n == 3:
            return n
        else:
            curr_len = 2
            step = 2
            paste_len = 1
            while curr_len < n:
                if n % curr_len == 0:
                    paste_len = curr_len
                    curr_len += paste_len
                    step += 2
                else:
                    curr_len += paste_len
                    step += 1
            return step

