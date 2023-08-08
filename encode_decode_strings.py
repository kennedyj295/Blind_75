# start = ['lint', 'code', 'love', 'you']
encoded = "4#lint4#code4#love3#you"
# encoded = ''
#
i = 0
j = 0
final = []
# res = []
#
# for s in start:
#     encoded = encoded + str(len(s)) + '#' + s
#
# print(encoded)

while i < len(encoded):
    j = i
    while encoded[j] != '#':
        j += 1
        print(j)
    nextStringLength = int(encoded[i:j])
    toBeAdded = encoded[j + 1:j + 1 + nextStringLength]
    final.append(toBeAdded)
    i = j + 1 + nextStringLength
print(final)

