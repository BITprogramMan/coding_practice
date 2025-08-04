from typing import Optional

class TreeNode:
    def __init__(self, happy=0, employees=[]):
        self.happy = happy
        self.employees = employees

class Solution:
    def findMaxHappy(self, root: Optional[TreeNode]) -> int:
        def traval(root, is_go):
            if not root.employees:
                return root.happy if is_go else 0
            else:
                maxHappy = 0
                if is_go:
                    for employee in root.employees:
                        maxHappy += traval(employee, not is_go)
                else:
                     for employee in root.employees:
                         maxHappy += max(traval(employee, not is_go), traval(employee, is_go))
                return maxHappy
        if not root:
            return 0
        return max(traval(root, True), traval(root, False))
                         
