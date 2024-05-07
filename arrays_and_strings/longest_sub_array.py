# Given an array of positive integers nums and an integer k,
# find the length of the longest subarray whose sum is less than or equal to k.

def find_length(nums, k):
    curr = left = ans = 0
    for right in range(len(nums)):
        curr += nums[right]
        while curr < k:
            left += 1
            curr -= nums[left]
        ans = max(ans, right - left + 1)
    return ans

# O(n) time
# O(1) space
