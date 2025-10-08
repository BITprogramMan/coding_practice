class Solution:

    def get_max_length(self, arr, k):
        if not arr or k <= 0:
            return 0
        left = 0
        right = 0
        current_sum = arr[0]
        max_len = 0

        while right < len(arr):
            if current_sum == k:
                max_len = max(max_len, right - left + 1)
                current_sum -= arr[left]
                left += 1
            elif current_sum < k:
                right += 1
                if right == len(arr):
                    break
                current_sum += arr[right]
            else:  # current_sum > k
                current_sum -= arr[left]
                left += 1

        return max_len
