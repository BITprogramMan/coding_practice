class Solution:
    """
    给定一个只由 0(假)、1(真)、&(逻辑与)、|(逻辑或)和^(异或)五种字符组成
    的字符串express，再给定一个布尔值 desired。返回express能有多少种组合
    方式，可以达到desired的结果。
    【举例】
    express="1^0|0|1"，desired=false
    只有 1^((0|0)|1)和 1^(0|(0|1))的组合可以得到 false，返回 2。
    express="1"，desired=false
    无组合则可以得到false，返回0
    """
    def process(self, express, desired):
        def isValid(express):
            n = len(express)
            if n & 1 == 0:
                return False
            for i in range(1, n, 2):
                if express[i - 1] != 0 and express[i - 1] != 1:
                    return False
                if express[i] != '^' and express[i] != '|' and express[i] != '&':
                    return False
            return True
        
        def count_ways(l, r, express, desired):
            if l == r:
                if express[l] == '0':
                    return 1 if not desired else 0
                else:
                    return 0 if not desired else 1
            res = 0
            for i in range(l + 1, r, 2):
                if desired:
                    if express[i] == '&':
                        res += count_ways(l, i - 1, express, desired) * count_ways(i + 1, r, express, desired)
                    elif express[i] == '|':
                        ways1 = count_ways(l, i - 1, express, desired)
                        ways2 = count_ways(l, i - 1, express, not desired)
                        ways3 = count_ways(i + 1, r, express, desired)
                        ways4 = count_ways(i + 1, r, express, not desired)
                        res += ways1 * (ways3 + ways4) + ways2 * ways3
                    else:
                        ways1 = count_ways(l, i - 1, express, desired)
                        ways2 = count_ways(l, i - 1, express, not desired)
                        ways3 = count_ways(i + 1, r, express, desired)
                        ways4 = count_ways(i + 1, r, express, not desired)
                        res += ways1 * ways4 + ways2 * ways3
                else:
                    if express[i] == '&':
                        ways1 = count_ways(l, i - 1, express, desired)
                        ways2 = count_ways(l, i - 1, express, not desired)
                        ways3 = count_ways(i + 1, r, express, desired)
                        ways4 = count_ways(i + 1, r, express, not desired)
                        res += ways1 * (ways3 + ways4) + ways2 * ways3
                    elif express[i] == '|':
                        res += count_ways(l, i - 1, express, desired) * count_ways(i + 1, r, express, desired)
                    else:
                        ways1 = count_ways(l, i - 1, express, desired)
                        ways2 = count_ways(l, i - 1, express, not desired)
                        ways3 = count_ways(i + 1, r, express, desired)
                        ways4 = count_ways(i + 1, r, express, not desired)
                        res += ways1 * ways3 + ways2 * ways4
            return res
                     



        if not isValid(express) or express is None or len(express) < 1 :
            return 0

        return count_ways(0, len(express) - 1, express, desired)


    def processv1(self, express, desired):
        def isValid(express):
            n = len(express)
            if n & 1 == 0:
                return False
            for i in range(1, n, 2):
                if express[i - 1] != 0 and express[i - 1] != 1:
                    return False
                if express[i] != '^' and express[i] != '|' and express[i] != '&':
                    return False
            return True
        if not isValid(express) or express is None or len(express) < 1 :
            return 0
        
        n = len(express)
        true_dp = [[0] * n for _ in range(n)]
        false_dp = [[0] * n for _ in range(n)]
        true_dp[0][0] = 1 if express[0] == '1' else 0
        false_dp[0][0] == 1 if express[0] == '0' else 0
        for i in range(2, n, 2):
            true_dp[i][i] = 1 if express[i] == '1' else 0
            false_dp[i][i] = 1 if express[i] == '0' else 0
            for j in range(i - 2, -1, -2):
                for k in range(j, i, 2):
                    if express[k + 1] == '&':
                        true_dp[j][i] += true_dp[j][k] * true_dp[k + 2][i]
                        false_dp[j][i] += (false_dp[j][k] + true_dp[j][k]) * false_dp[k + 2][i] + false_dp[j][k] + true_dp[k + 2][i] 

                    elif express[k + 1] == '|':
                        true_dp[j][i] += (false_dp[j][k] + true_dp[j][k]) * true_dp[k + 2][i] + true_dp[j][k] * false_dp[k + 2][i]
                        false_dp[j][i] += false_dp[j][k] * false_dp[k + 2][i]
                    
                    else:
                        true_dp[j][i] += false_dp[j][k] * true_dp[k + 2][i] + true_dp[j][k] * false_dp[j][k] * true_dp[k + 2][i]
                        false_dp[j][i] += false_dp[j][k] * false_dp[k + 2][i] + true_dp[j][k] * true_dp[k + 2][i]
                
        if desired:
            return true_dp[0][n - 1]
        else:
            return false_dp[0][n - 1]
        












