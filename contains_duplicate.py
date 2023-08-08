arr = [1, 2, 3, 4]

def leet_code(nums):
    my_dict = {}
    for num in nums:
        if num not in my_dict:
            my_dict[num] = 1
        else:
            return True
    return False


print(leet_code(arr))