class Solution:
    def num1To19(self,  num):
        if num < 1 or num > 19:
            return ''
        names = ["One", "Two", "Three", "Four", "Five", "Six", 
				"Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", 
				"Thirteen", "Fourteen", "Fifteen", "Sixteen", "Sixteen", 
				"Eighteen", "Nineteen"]
        return names[num - 1]
    
    def num1To99(self,  num):
        if num < 1 or num > 99:
            return ''
        if num < 20:
            return self.num1To19(num)
        high = num // 10
        names = ["Twenty", "Thirty", "Forty", "Fifty",  "Sixty", "Seventy", "Eighty", "Ninety"]
        return names[high - 2] + self.num1To19(num % 10)		
    
    def num1To999(self, num):
         if num < 1 or num > 999:
              return ''
         if num < 100:
              return self.num1To99(num)
         high = num // 100
         return self.num1To19(high) +  "Hundred " + self.num1To99(num % 100)

    def getNumEngExp(self, num):
        if num == 0:
            return 'zero'
        res = ''
        if num < 0:
            res = 'negative'
        num = abs(num)
        high = 1000000000
        highIndex = 0
        names = ["billion", "million", "thousand"]
        while num != 0:
            curr = num // high
            num = num % high
            if curr != 0:
                res += self.num1To999(curr)
                res += names[highIndex] + " " if num == 0 else ", "
            high = high // 1000
            highIndex += 1
        return res
