class Solution:
    """
    给定一个 N×3 的矩阵 matrix，对于每一个长度为 3 的小数组 arr，都表示一个大楼的三个数
    据。arr[0]表示大楼的左边界，arr[1]表示大楼的右边界，arr[2]表示大楼的高度(一定大于 0)。
    每座大楼的地基都在 X 轴上，大楼之间可能会有重叠，请返回整体的轮廓线数组。
    【举例】
    matrix = {
    {2,5,6},
    {1,7,4},
    {4,6,7},
    {3,6,5},
    {10,13,2},
    {9,11,3},
    {12,14,4},
    {10,12,5}
    }
    返回：
    {{1,2,4},
    {2,4,6},
    {4,6,7},
    {6,7,4},
    {9,10,3},
    {10,12,5},
    {12,14,4
    """
    def process(self, matrix):
        
        height_count_dict = {}
        max_height_dict = {}
        n = len(matrix)
        record = []
        for i in range(n):
            record.append([matrix[i][0], 'a', matrix[i][2]])
            record.append([matrix[i][1], 'd', matrix[i][2]])
        record.sort(key=lambda x: (x[0], x[1]))
        
        for i in range(2 * n):
            if record[i][1] == 'a':
                height_count_dict[record[i][2]] = height_count_dict.get(record[i][2], 0) + 1
            else:
                height_count_dict[record[i][2]] -= 1
                if height_count_dict[record[i][2]] == 0:
                    del height_count_dict[record[i][2]]
            current_max = max(height_count_dict.keys()) if height_count_dict else 0
            max_height_dict[record[i][0]] = current_max
        res = []
        sorted_x = sorted(max_height_dict.keys())
        start = sorted_x[0]
        prev_height = max_height_dict[start]
        for i in range(1, len(sorted_x)):
            curr_x = sorted_x[i]
            if max_height_dict[curr_x] != prev_height:
                if prev_height != 0:
                    res.append([start, curr_x, prev_height])
                prev_height = max_height_dict[curr_x]
                start = curr_x
        return res
            
