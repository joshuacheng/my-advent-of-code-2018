freqs = open("input.txt")

values = freqs.read()
values = values.split('\n')

count = 0

# print(values)

for freq in values:
    if len(freq) > 0:
        if freq[0] == '+':
            count += int(freq[1:])
        else:
            count -= int(freq[1:])

print(count)
