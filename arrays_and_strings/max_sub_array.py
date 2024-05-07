from typing import List
# 643. Maximum Average Subarray I


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window = sum(nums[:k])
        max_window = window
        for i in range(len(nums) - k):
            window = window - nums[i] + nums[i + k]
            max_window = max(max_window, window)
        return max_window / k
