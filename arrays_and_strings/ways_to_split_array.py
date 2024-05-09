from typing import List
# 2270. Number of Ways to Split Array
# Given an integer array nums,
# find the number of ways to split the array into two parts
# so that the first section has a sum greater than or equal to the sum of the second section.
# The second section should have at least one number.


class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        # declare prefix sum
        prefix = [nums[0]]
        # build prefix sum
        for i in range(1, n):
            prefix.append(nums[i] + prefix[-1])
        # get the splits
        for i in range(n - 1):
            # check sum of first and second splits
            first_split = prefix[i]
            second_split = prefix[n-1] - first_split
            if first_split >= second_split:
                count += 1
        return count
