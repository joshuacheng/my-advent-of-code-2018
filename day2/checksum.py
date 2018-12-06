import collections

file = open('input.txt')

ids = file.read().split('\n')
ids.pop()

numthrees = numtwos = 0

for id in ids:
    lookingthree = lookingtwo = True

    # Counter is basically a word freq dict of a word
    letters = collections.Counter(id)
    for letter, count in letters.most_common():
        if not lookingthree and not lookingtwo:
            break
        if count == 3 and lookingthree:
            numthrees += 1
            lookingthree = False
        if count == 2 and lookingtwo:
            numtwos += 1
            lookingtwo = False
    
# numthrees * numtwos is our checksum
print(numthrees * numtwos)