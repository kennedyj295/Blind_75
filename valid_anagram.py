

def valid_anagram (t, s):
    mapT, mapS = {}, {}

    if (len(t) != len(s)):
        return False
    else:
        for i in range(len(t)):
            if (t[i] not in mapT):
                mapT[t[i]] = 1
            else:
                mapT[t[i]] += 1

            if (s[i] not in mapS):
                mapS[s[i]] = 1
            else:
                mapS[s[i]] += 1

    for key, value in mapT.items():
        if (key in mapS and value == mapS[key]):
            continue
        else:
            return False

    return True
