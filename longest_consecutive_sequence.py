longest = 0
nums = [100,4,200,1,3,2]

iterateOverMe = set(nums)

for item in iterateOverMe:
    if (item - 1 not in iterateOverMe):
        length = 0
        while (item + length in iterateOverMe):
            length += 1
        longest = max(length, longest)
print(longest)