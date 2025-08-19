class Solution:
    def maxValue(self, weights, values, bag):
        def process(index, alreadtWeight, bag, n, weights, values):
            if alreadtWeight > bag:
                return -1
            if index == n:
                return 0
            p1 = process(index + 1, alreadtWeight, bag,n ,weights, values)
            if alreadtWeight + weights[index] <= bag:
                return max(p1, process(index + 1, alreadtWeight + weights[index], bag, n, weights, values))
            else:
                return p1
        

        