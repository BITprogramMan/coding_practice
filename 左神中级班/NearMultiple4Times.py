class Solution:
    """
    给定一个数组arr，如果通过调整可以做到arr中任意两个相邻的数字相乘是4的倍数，
    返回true；如果不能返回false
    """
    def NearMultiple4Times(self, nums):
        count = {'odd': 0, '2times': 0, '4times': 0}
        for num in nums:
            if num & 1 == 1:
                count['odd'] += 1
            elif (num & (num - 1)) == 0 and (num & 0xaaaaaaaa) == 0:
                count['4times'] += 1
            else:
                count['2times'] += 1
        if count['2times'] == 0:
            if count['odd'] == 1:
                return count['4times'] >= 1
            else:
                return count['4times'] >= count['odd'] - 1
        else:
            if count['2times'] & 1 == 1:
                return count['4times'] >= 1 and count['4times'] >= count['odd']
            else:
                return count['4times'] >= count['odd']
