import re
from collections import defaultdict
from operator import itemgetter
from functools import reduce

timeRegex = re.compile(r'\[(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2})\] (.+)')

file = open('input.txt')
notes = file.read().split('\n')
notes.pop()
notesAsTuples = []

# Converts input to int if less than 5 chars long
def tryConvertInt(input):
    if (len(input) > 4):
        return input
    else:
        return int(input)

for note in notes:
    # time is a tuple of (year, month, day, hour, min)
    timeTuple = timeRegex.search(note).groups()
    notesAsTuples.append(tuple(map(tryConvertInt, timeTuple)))

notesAsTuples = sorted(notesAsTuples, key=itemgetter(0, 1, 2, 3, 4))

count = 0
for i in range(len(notesAsTuples) - 1):
    if (notesAsTuples[i][5][0:5] == 'falls' and notesAsTuples[i + 1][5][0:5] == 'Guard'):
        count += 1

print(count)

'''
    Each guard is a key to a dict, each entry is total minutes they've slept
    as well as another dictionary of each minute they spent asleep
'''
guardDict = {}
guardIDRegex = re.compile('#(\d{1,4})')

# Populate guard dict
for idx, note in enumerate(notesAsTuples):
    msg = note[5]
    # Start a new guard entry
    if msg[0:5] == 'Guard':
        guardID = guardIDRegex.search(msg).group(1)
        # Account for guards who start early
        if note[3] == 23:
            min = 0
        else:
            min = note[4]
        
        if guardID not in guardDict:
            guardDict[guardID] = defaultdict(int)
        continue
    
    # Add awake / sleep times
    if msg[0:5] == 'falls':
        min = note[4]

    if msg[0:5] == 'wakes':
        while min < note[4]:
            guardDict[guardID][min] += 1
            min += 1

# print(guardDict)
guardToMinutesDict = {}

for guardID, minutesDict in guardDict.items():
    guardToMinutesDict[guardID] = reduce(lambda x,y: x + y, minutesDict.values(), 0)
    
# Part 1
# mostWorkGuard = sorted(guardToMinutesDict.items(), key=itemgetter(1), reverse=True)[0][0]
# mostMinute = sorted(guardDict[mostWorkGuard].items(), key=itemgetter(1), reverse=True)[0][0]
# print(int(mostWorkGuard) * int(mostMinute))
# Part 1

# Part 2
decorated = list(filter(lambda x: len(x[1]) > 0, [(id, sorted(mins.items(), key=itemgetter(1), reverse=True)) for id, mins in guardDict.items()]))
decorated = sorted(decorated, key=lambda x: x[1][0][1], reverse=True)
mostSleepGuard = int(decorated[0][0])
mostSleepMinute = decorated[0][1][0][0]
print(mostSleepGuard * mostSleepMinute)
# print([(id, mins) for mins, id in decorated])