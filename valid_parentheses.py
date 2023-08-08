s = "([{}])"

charMap = {")": "(", "]": "[", "}": "{"}
popStack = []

for c in s:
    if c in charMap:
        if popStack and popStack[-1] == charMap[c]:
            popStack.pop()
        else:
            print("false")
    else:
        popStack.append(c)
print("true") if not popStack else print("false")
