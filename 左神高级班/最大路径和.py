class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    给定一棵二叉树的头节点head，可以从树中的任何一点出发，如果走的话只能向下，
    也可以选择随时停止，所形成的轨迹叫做一条路径，路径上所有值的累加和叫作路径
    和。求这棵树上的最大路径和。
    """
    # def maxPathSum(self, head):
    #     if not head:
    #         return 0
    #     def process(head):
    #         if not head:
    #             return 0, 0, float('-inf')
    #         leftInfo = process(head.left)
    #         rightInfo = process(head.right)
    #         maxValue = max([head.val, leftInfo[-1], rightInfo[-1]])
    #         maxPathSumHead = max([leftInfo[-2] + head.val, rightInfo[-2] + head.val, head.val])
    #         maxPathSumAll = max([leftInfo[0], rightInfo[0], maxPathSumHead])
    #         return maxPathSumAll, maxPathSumHead, maxValue
            
    #     allData = process(head)
    #     return allData[-1] if allData[-1] < 0 else allData[0]   #最大值的记录好像是不必要的


    def maxPathSum(self, head):
        if not head:
            return 0
        def process(head):
            if not head:
                return 0, 0
            leftInfo = process(head.left)
            rightInfo = process(head.right)
            maxPathSumHead = max([leftInfo[-1] + head.val, rightInfo[-1] + head.val, head.val])
            maxPathSumAll = max([leftInfo[0], rightInfo[0], maxPathSumHead])
            return maxPathSumAll, maxPathSumHead
            
        allData = process(head)
        return allData[-1] if allData[-1] < 0 else allData[0]


    

if __name__ == '__main__':
    solution = Solution()
    node1 = TreeNode(val=-2)
    node1.left = TreeNode(val=-5)
    node1.right = TreeNode(val=-10)
    print(solution.maxPathSum(node1))


