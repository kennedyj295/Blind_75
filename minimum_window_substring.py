s = "ADOBECODEBANC"
t = "ABC"

if t == "": print("")

countT, window = {}, {}
#CounT stores the counts of characters in t
#window stores the counts of characters in the current window

for c in t:
    countT[c] = 1 + countT.get(c, 0)
#counts the occurences of each character in t

have, need = 0, len(countT)
#have stores the number of needed characters are present in the current window
#need stores the number of needed characters

res, resLen = [-1, -1], float("infinity")
l = 0
#res will store the start and end indices of the minimum window, resLen will store its length

for r in range(len(s)):
# r represents the end of the current window
    c = s[r]
    window[c] = 1 + window.get(c, 0)
    #in the window dictionary, increments the count of the character at the right pointer

    if c in countT and window[c] == countT[c]:
        have += 1
    #if the character is in t and its count in the current window matches its count in t, have is incremented

    while have == need:
    #runs when all the unique characters from t are present in the current window of s
        if (r - l + 1) < resLen:
        #checks if the current window's length is less than the current minimum length
            res = [l, r]
            resLen = (r - 1 + 1)
            # updates the result if a shorter window is found
        window[s[l]] -= 1
        # decrements the count of the character at the left pointer
        if s[l] in countT and window[s[l]] < countT[s[l]]:
        #if the character decremented in the window is in t and the count no longer matches what's required, have variable is decremented
            have -= 1
        l += 1
        #moves the left pointer to the right, shrinking the window

    l, r = res
    # return s[l:r+1] if resLen != float("infinity")

