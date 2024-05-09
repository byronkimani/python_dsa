# Given an integer array nums, an array queries where queries[i] = [x, y] and an integer limit,
# return a boolean array that represents the answer to each query.
# A query is true if the sum of the subarray from x to y is less than limit, or false otherwise.
# For example, given nums = [1, 6, 3, 2, 7, 2], queries = [[0, 3], [2, 5], [2, 4]], and limit = 13,
# the answer is [true, false, true]. For each query, the subarray sums are [12, 14, 12].

def answer_queries(nums, queries, limit):
    ans = []
    # build prefix sum
    pref = [nums[0]]
    for i in range(1, len(nums)):
        pref.append(nums[i] + pref[i-1])
    # iterate over queries to evaluate them
    for query in queries:
        # query[0] = start of sub array
        # query[1] = end of sub array
        # find sum of sub_array
        sub_array_sum = pref[query[1]] - pref[query[0]] + nums[query[0]]
        if sub_array_sum < limit:
            ans.append(True)
        else:
            ans.append(False)
    return ans


nums = [1, 6, 3, 2, 7, 2]
queries = [[0, 3], [2, 5], [2, 4]]
limit = 13
print(answer_queries(nums, queries, limit))
# O(n+m) time where n is length of nums and m is length of queries
# O(n) space
# Use prefix sum to solve the problem
