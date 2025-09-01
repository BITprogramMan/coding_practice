class Solution:
    """
    给定一个数组arr，长度为N且每个值都是正数，代表N个人的体重。再给定一个正数
    limit，代表一艘船的载重。以下是坐船规则，1）每艘船最多只能做两人；2）乘客
    的体重和不能超过limit。返回如果同时让这N个人过河最少需要几条船。
    """
    def minBoat(self, arr, weight):
        if len(arr) < 1:
            return 0
        arr.sort()
        if arr[-1] > weight:
            return -1
        if arr[-1] <= weight / 2:
            return (len(arr) + 1) // 2
        if arr[0] > weight / 2:
            return len(arr)
        l, r = -1, -1
        n = len(arr)
        for i in range(n):
            if arr[i] <= weight / 2 and (i + 1 == n or arr[i + 1] > weight / 2):
                l, r = i, i + 1
        ans = 0
        unfinished_l = 0
        while l >= 0 and r < n:
            if arr[l] + arr[r] <= weight:
                ans += 1
                l -= 1
                r += 1
            else:
                unfinished_l += 1
                l -= 1
        if l >= 0:
            unfinished_l += (l + 1)
        ans += (unfinished_l + 1) // 2
        ans += (n - r)
        return ans



