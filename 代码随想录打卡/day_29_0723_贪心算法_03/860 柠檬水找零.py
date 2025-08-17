from typing import List

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        num_money_5 = 0
        num_money_10 = 0
        for i in range(len(bills)):
            if bills[i] == 5:
                num_money_5 += 1
            elif bills[i] == 10:
                num_money_5 -= 1
                num_money_10 += 1
            else:
                if num_money_10 > 0:
                    num_money_10 -= 1
                    num_money_5 -= 1
                else:
                    num_money_5 -= 3
            if num_money_5 < 0:
                return False
        return True
