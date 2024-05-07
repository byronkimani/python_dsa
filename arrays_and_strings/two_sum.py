# nums is sorted
def check_for_target(nums, target):
    start = 0
    end = len(nums) - 1

    while start < end:
        total = nums[start] + nums[end]
        if total == target:
            return True
        elif total < target:
            start += 1
        else:
            end -= 1
    return False
# O(n) time
# O(1) space


value = check_for_target([1, 2, 4, 6, 8, 9, 14, 15], 13)
print(value)
# To note
# Name variables well
