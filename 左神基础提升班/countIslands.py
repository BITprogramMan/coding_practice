def countIslands(nums):
    if not nums or not nums[0]:
        return 0
    def infect(i, j, nums, m, n):
        if i < 0 or i >=m or j < 0 or j >= n or nums[i][j] != 1:
            return 
        nums[i][j] = 2
        infect(i + 1, j ,nums, m, n)
        infect(i - 1, j, nums, m, n)
        infect(i, j - 1, nums, m, n)
        infect(i, j + 1, nums, m, n)


    m, n = len(nums), len(nums[0])
    res = 0
    for i in range(m):
        for j in range(n):
            if nums[i][j] == 1:
                res += 1
                infect(i, j, nums, m, n)
    return res


        