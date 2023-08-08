inpStr = "abcabcbb"

mySet = set()
res = 0
l = 0

for r in range(len(inpStr)):
    while (inpStr[r] in mySet):
        mySet.remove(inpStr[l])
        l += 1
    mySet.add(inpStr[r])
    res = max(res, r - l + 1)

print(res)