class Solution:
    """
    一个数组中只有两种字符'G'和'B'，
    想让所有的的G都放在左侧，所有的B都放在右侧;或者所有的B放左侧，所有的G放右侧
    但是只能在相邻字符之间进行交换操作，
    返回至少需要交换几次
    """
    def minSwap(self, nums):
        gi, bi = 0, 0
        step1, step2 = 0, 0
        for i in range(len(nums)):
            if nums[i] == 'G':
                step1 += (i - gi)
                gi += 1
            else:
                step2 += (i - bi)
                bi += 1
        return min(step1, step2)
    

    