from string import ascii_lowercase
import sys
import re

file = open('input.txt')
polymer = file.read()

# Use list as stack - only use append(item) and pop()

def oppositeCase(char1, char2):
    if (char1.isupper() and char2 == char1.lower() or
       char1.islower() and char2 == char1.upper()):
       return True
    return False

def last(stk):
    if (len(stk) == 0):
        return ''
    return stk[len(stk) - 1]


'''
    Takes in an unreacted polymer and an optional string whose instances will
    be removed before reacting the polymer.
    Returns the reacted polymer string
'''
def reactPolymer(unReacted, str=''):
    findStrRegex = re.escape(str) + r'|' + re.escape(str.upper())
    stack = []
    idx = 0

    if str != '':
        unReacted = re.sub(findStrRegex, '', unReacted)

    while idx < len(unReacted) - 1:

        if not oppositeCase(last(stack), unReacted[idx]):
            stack.append(unReacted[idx])
            idx += 1
            continue

        oppositeCount = 1
        while oppositeCase(last(stack), unReacted[idx]):
            idx += 1
            oppositeCount += 1
            stack.append(unReacted[idx])     

        # pop off the destroyed polymer pair/triplets
        for i in range(oppositeCount):
            stack.pop()
    
    return ''.join(stack)



# Part 1
# result = reactPolymer(polymer)
# print(len(result))
# Part 1


# Part 2 loop through all alphabet characters, delete them from polymer, and react polymers that way
# pretty inefficient but I can't think of a better way off the top of my head
shortestLength = sys.maxsize
for c in ascii_lowercase:
    currLength = len(reactPolymer(polymer, c))
    if currLength < shortestLength:
        shortestLength = currLength

print(shortestLength)




