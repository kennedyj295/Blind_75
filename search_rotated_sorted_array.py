nums = [4, 5, 6, 7, 0, 1, 2]
target = 0

l, r = 0, len(nums) - 1

while l <= r:
    mid = (l + r) // 2
    if target == nums[mid]:
        print(str(mid))
        exit()

    if nums[l] <= nums[mid]:
    #checking whether target might be in the left half
    #if the left half of the current range is sorted such that nums[l] <= nums[mid]
    #the code checks whether the target is in that sorted left half or unsorted right half
        if target > nums[mid] or target < nums[l]:
        #if the target is greater than nums[mid] or less than nums[l], the target must be in the unsorted right half, so l is updated to mid + 1
            l = mid + 1
        else:
        #Otherwise, the target must be in the sorted left half, so r is updated to mid - 1
            r = mid - 1
    else:
        if target < nums[mid] or target > nums[r]:
        #if the target is less than nums[mid] or greater than nums[r] the target must be in
        #the unsorted left half, so r is updated to mid - 1
            r = mid - 1
        else:
        #otherwise the target must be in the sorted right half, so l is updated to mid + 1
            l = mid + 1

print("-1")

