class Solution:
    def get_max(self, n1, n2):
        sign = self.get_fign(n1 - n2) # 符号不同在C语言中存在溢出风险
        return sign * n1 + self.flip(sign) * n2


    def flip(self, n):
        return n ^ 1
    
    def get_fign(self, n):
        return self.flip((n >> 31) & 1)
    

    def get_maxv1(self, n1, n2):
        sign1 = self.get_fign(n1)
        sign2 = self.get_fign(n2)
        diffSign = sign1 ^ sign2
        sameSign = self.flip(diffSign)
        return1 = sameSign * self.get_fign(n1 - n2) + diffSign * sign1
        return2 = self.flip(return1)
        return return1 * n1 + return2 * n2 # 利用加号，把互斥条件的if else写成数学的形式