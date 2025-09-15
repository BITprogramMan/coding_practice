class Solution:
    """
    假设s和m初始化，s = "a"; m = s;
    再定义两种操作，第一种操作：
    m = s;
    s = s + s;
    第二种操作：
    s = s + m;
    求最小的操作步骤数，可以将s拼接到长度等于n
    """
    def minOps(self, n):
        s_len, m_len = 1, 1
        operations = 0
        while s_len < n:
            if n % s_len == 0:
                m_len = s_len
                s_len = s_len * 2
                operations += 1
            else:
                s_len += m_len
                operations += 1
        return operations
    
    def minOpsv1(self, n):

        def is_prim(n):
            if n < 2:
                return False
            max_divisor = int(n ** 0.5)
            for i in range(2, max_divisor + 1):
                if n % i == 0:
                    return False
            return True
        
        def divs_sum_and_count(n):
            sum_factors = 0
            count_factors = 0
            for i in range(2, n + 1):
                while n % i == 0:
                    sum_factors += i
                    count_factors += 1
                    n = n // i
            return sum_factors, count_factors
        
        if n < 2:
            return 0
        if is_prim(n):
            return n - 1
        sum_factors, count_factors = divs_sum_and_count(n)
        return sum_factors - count_factors





