class Solution:
    """
    如果一个字符串为str，把字符串str前面任意的部分挪到后面形成的字符串叫
    作str的旋转词。比如str="12345"，str的旋转词有"12345"、"23451"、
    "34512"、"45123"和"51234"。给定两个字符串a和b，请判断a和b是否互为旋转
    词。
    比如：
    a="cdab"，b="abcd"，返回true。
    a="1ab2"，b="ab12"，返回false。
    a="2ab1"，b="ab12"，返回true。
    """
    def IsRotation(self, s, goal):
        n1, n2 = len(s), len(goal)
        if n1 != n2:
            return False
        for i in range(n1):
            flag = 1
            for j in range(n2):
                if s[(i + j) % n1] != goal[j]:
                    flag = 0
                    break
            if flag == 1:
                return True
        return False
    
    def IsRotationv1(self, s, goal):
        return len(s) == len(goal) and goal in s + s

    def IsRotationv2(self, s, goal):
        """手动实现KMP"""
        def getNextArray(target):
            n = len(target)
            res = [0] * n
            res[0] = -1
            cn = 0
            index = 2
            while index < n:
                if target[index - 1] == target[cn]:
                    cn += 1
                    res[index] = cn
                    index += 1
                elif cn > 0:
                    cn = res[cn]
                else:
                    index += 1
            return res

        def getIndex(s1, s2):
            nexts = getNextArray(s2)
            n1, n2 = len(s1), len(s2)
            index1, index2 = 0, 0
            while index1 < n1 and index2 < n2:
                if s1[index1] == s2[index2]:
                    index1 += 1
                    index2 += 1
                elif index2 > 0:
                    index2 = nexts[index2]
                else:
                    index1 += 1
            return True if index2 == n2 else False
        return len(s) == len(goal) and getIndex(s + s, goal)




        


  
if __name__ == '__main__':
    solution = Solution()
    print(solution.IsRotation('abcde', 'cdeab'))