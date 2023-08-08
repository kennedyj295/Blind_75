class Solution(object):
    def topKFrequent(self, nums, k):
        checker = {}
        otherChecker = [[] for i in range(len(nums) + 1)]

        for num in nums:
            checker[num] = checker.get(num, 0) + 1
        for key, value in checker.items():
            otherChecker[value].append(key)

        result = []

        for i in range(len(otherChecker) - 1, 0, -1):
            for num in otherChecker[i]:
                result.append(num)
                if len(result) == k:
                    return result




