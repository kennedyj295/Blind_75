nums = [0, -1, 2, 4, 0]
res = []
res = []
nums.sort()

for i, a in enumerate(nums):
    if a > 0:
        break

    if i > 0 and a == nums[i - 1]:
        continue

    l = i + 1
    r = len(nums) - 1

    while l < r:
        threeSum = a + nums[l] + nums[r]
        if threeSum > 0:
            r -= 1
        elif threeSum < 0:
            l += 1
        else:
            holder = [nums[i], nums[r], nums[l]]
            res.append(holder)
            l += 1
            r -= 1
            while nums[l] == nums[l - 1] and l < r:
                l += 1
print(res)