class Solution:
    def maxValue(self, weights, values, bag):
        def process(index, alreadtWeight, bag, n, weights, values):
            if alreadtWeight > bag:
                return 0
            if index == n:
                return 0
            return max(process(index + 1, alreadtWeight, bag,n ,weights, values), values[index] + process(index + 1, alreadtWeight + weights[index], bag, n, weights, values))
        

        