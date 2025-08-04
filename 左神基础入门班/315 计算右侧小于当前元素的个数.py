from typing import List

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        final_res = [0] * n
        if n < 2:
            return final_res
        index_mapping = list(range(n))
        def merge(nums, l, mid, r):
            p1, p2 = l, mid + 1
            res = []
            res_index = []
            while p1 <= mid and p2 <= r:
                if nums[p1] > nums[p2]:
                    final_res[index_mapping[p1]] += (r - p2 + 1) 
                    res.append(nums[p1])
                    res_index.append(index_mapping[p1])
                    p1 += 1
                else:
                    res.append(nums[p2])
                    res_index.append(index_mapping[p2])
                    p2 += 1
            while p1 <= mid:
                    res.append(nums[p1])
                    res_index.append(index_mapping[p1])
                    p1 += 1
            while p2 <= r:
                res.append(nums[p2])
                res_index.append(index_mapping[p2])
                p2 += 1
            for i in range(len(res)):
                nums[l + i] = res[i]
                index_mapping[l + i] = res_index[i]

        def mergev1(nums, l, mid, r):
            p1, p2 = l, mid + 1
            res = []
            res_index = []
            while p1 <= mid and p2 <= r:
                if nums[p1] <= nums[p2]:
                    final_res[index_mapping[p1]] += (p2 - mid -1) 
                    res.append(nums[p1])
                    res_index.append(index_mapping[p1])
                    p1 += 1
                else:
                    res.append(nums[p2])
                    res_index.append(index_mapping[p2])
                    p2 += 1
            while p1 <= mid:
                    res.append(nums[p1])
                    final_res[index_mapping[p1]] += (p2 - mid - 1) 
                    res_index.append(index_mapping[p1])
                    p1 += 1
            while p2 <= r:
                res.append(nums[p2])
                res_index.append(index_mapping[p2])
                p2 += 1
            for i in range(len(res)):
                nums[l + i] = res[i]
                index_mapping[l + i] = res_index[i]


        def merge_sort(nums, l, r):
            if l == r:
                return 
            else:
                mid = l + (r - l) // 2
                merge_sort(nums, l, mid)
                merge_sort(nums, mid + 1, r)
                merge(nums, l, mid, r)
        merge_sort(nums, 0, len(nums) - 1)
        print(nums)
        print(index_mapping)
        return final_res
    

if __name__ =='__main__':
    solution = Solution()   
    nums = [1, 9, 7, 8, 5]
    print(nums)
    res =solution.countSmaller(nums)
    print(res)


