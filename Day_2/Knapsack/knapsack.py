import math
a = int(input())
output = ''
for i in range(a):
    n, W = list(map(int, input().split(' ')))
    w = list(map(int, input().split(' ')))
    c = 0
    index = []
    for j in range(len(w)):
        if c + w[j] <= W:
            c += w[j]
            index.append(str(j+1))
    if c < math.ceil(W/2):
        output += '-1\n'
    else:
        output += str(len(index)) + str('\n') + str(' '.join(index)) + str('\n')
print(output)