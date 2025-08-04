
class Solution:
    def printAllFolds(self, N):
        def printProcess(i, N, down):
            if i > N:
                return
            printProcess(i + 1, N, True)
            if down:
                print("凹")
            else:
                print("凸")
            printProcess(i + 1, N, False)
        printProcess(1, N, True)

