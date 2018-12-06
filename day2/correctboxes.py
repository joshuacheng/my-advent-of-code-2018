import collections

file = open('input.txt')

ids = file.read().split('\n')
ids.pop()

# Takes two words, assuming same length. If they differ by 1 char, returns index where. Otherwise, returns -1

def word_diffs(word_a, word_b):
    diffs = 0
    index = -1
    # Iterate over both words in parallel, comparing chars
    for c1, c2 in zip(enumerate(word_a), enumerate(word_b)):
        if c1[1] != c2[1]:
            diffs += 1
            index = c1[0]
        if diffs > 1:
            return -1
    return index

# print(word_diffs('abcde', 'abcaw'))

for i in range(len(ids)):
    for j in range(i + 1, len(ids)):
        index = word_diffs(ids[i], ids[j])
        if index >= 0:
            answer = open('answer.txt', 'w')
            answer.write(ids[i][0:index] + ids[i][index + 1:])

