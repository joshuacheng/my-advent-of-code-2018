

file = open('input.txt')
polymer = file.read()

# Use list as stack - only use append(item) and pop()
stack = []

def oppositeCase(char1, char2):
    if (char1.isupper() and char2 == char1.lower() or
       char1.islower() and char2 == char1.upper()):
       return True
    return False

def last(stk):
    if (len(stk) == 0):
        return ''
    return stk[len(stk) - 1]


idx = 0
while idx < len(polymer) - 1:

    if not oppositeCase(last(stack), polymer[idx]):
        stack.append(polymer[idx])
        idx += 1
        continue

    oppositeCount = 1
    while oppositeCase(last(stack), polymer[idx]):
        idx += 1
        oppositeCount += 1
        stack.append(polymer[idx])     

    # pop off the destroyed polymer pair/triplets
    for i in range(oppositeCount):
        stack.pop()

result = ''.join(stack)
print(len(result))
        





