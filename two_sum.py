nums = [2,7,11,15]

def twoSum(nums, target):

    checker = {}

    for i in range(len(nums)):
        complement = target - nums[i]

        if (complement in checker):
            return [i, checker[complement]]
        else:
            checker[nums[i]] = i
    return False

twoSum(nums, 9)