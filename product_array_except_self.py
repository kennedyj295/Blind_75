nums = [1, 2, 3, 4]

inputLen = len(nums)
retArr = [1] * inputLen
prod = 1

# Calculate the products of all elements to the left of each element
for i in range(inputLen):
    retArr[i] *= prod
    prod *= nums[i]

# Reset the prod variable to calculate products to the right
prod = 1

# Calculate the products of all elements to the right of each element
for i in range(inputLen - 1, -1, -1):
    retArr[i] *= prod
    prod *= nums[i]

print(retArr)
