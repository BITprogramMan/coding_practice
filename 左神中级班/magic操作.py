class Solution:
    """
    给一个包含n个整数元素的集合a，一个包含m个整数元素的集合b。
    定义magic操作为，从一个集合中取出一个元素，放到另一个集合里，且操作过
    后每个集合的平均值都大大于于操作前。
    注意以下两点：
    1）不可以把一个集合的元素取空，这样就没有平均值了
    2）值为x的元素从集合b取出放入集合a，但集合a中已经有值为x的元素，则a的
    平均值不变（因为集合元素不会重复），b的平均值可能会改变（因为x被取出
    了）
    问最多可以进行多少次magic操作？
    """
    def max_ops(self, arr1, arr2):
        # 请保证 arr1 无重复值、arr2 中无重复值，且 arr1 和 arr2 肯定有数字
        def avg(sum_val, size):
            return sum_val / float(size)
        
        sum1 = sum(arr1)
        sum2 = sum(arr2)

        if avg(sum1, len(arr1)) == avg(sum2, len(arr2)):
            return 0

        # 确定哪个数组平均值更大
        if avg(sum1, len(arr1)) > avg(sum2, len(arr2)):
            arr_more = arr1
            sum_more = sum1
            arr_less = arr2
            sum_less = sum2
        else:
            arr_more = arr2
            sum_more = sum2
            arr_less = arr1
            sum_less = sum1

        # 对平均值大的数组排序（从小到大）
        arr_more = sorted(arr_more)
        set_less = set(arr_less)  # 平均值小的数组转为集合，用于快速查找

        more_size = len(arr_more)
        less_size = len(arr_less)
        ops = 0

        # 遍历平均值大的数组（已排序）
        for cur in arr_more:
            avg_more = avg(sum_more, more_size)
            avg_less = avg(sum_less, less_size)

            # 如果当前数满足：
            # 1. 小于大数组当前平均值
            # 2. 大于小数组当前平均值
            # 3. 不在小数组中（避免重复）
            if cur < avg_more and cur > avg_less and cur not in set_less:
                # 移动这个数：从大数组移到小数组
                sum_more -= cur
                more_size -= 1
                sum_less += cur
                less_size += 1
                set_less.add(cur)  # 加入小数组集合
                ops += 1

        return ops





# 测试
if __name__ == "__main__":
    arr1 = [1, 2, 5]
    arr2 = [2, 3, 4, 5, 6]
    solution = Solution()
    print(solution.max_ops(arr1, arr2))  # 输出应为 1