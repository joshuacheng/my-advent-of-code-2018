freqs = open("input.txt")

values = freqs.read()
values = values.split('\n')
# the last value is an empty string lol
values.pop()
print(values)
count = 0
freq_freqs = {}
done = False

while not done:
    # print('got here')
    for freq in values:
        if freq[0] == '+':
            count += int(freq[1:])
        else:
            count -= int(freq[1:])
        
        if count in freq_freqs:
            done = True
            break
        else:
            freq_freqs[count] = 1
        # print(count)

print(count)