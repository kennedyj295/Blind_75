input = "!caR"

l, r = 0, len(input) - 1

while l < r:
    while not input[l].isalnum() and l < r:
        l += 1
    while not input[r].isalnum() and r > l:
        r -= 1
    if input[l].lower() != input[r].lower():
        print("false")
    l, r = l + 1, r -1
print("true")

