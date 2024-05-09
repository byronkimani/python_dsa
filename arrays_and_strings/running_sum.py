from typing import List
# 1480. Running Sum of 1d Array

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = [nums[0]]
        for i in range(1, len(nums) ):
            ans.append(nums[i] + ans[-1])
        return ans