t = int(input())
output = []
for i in range(t):
    n = int(input())
    a = list(map(int, input().split(' ')))
    tot = 0
    for j in range(1, len(a)):
        tot += abs(a[j] - a[j-1])
    if n==2:
        output.append(0)
        continue
    mx2 = 0
    mx2 = max(mx2, abs(a[0] - a[1]))
    mx2 = max(mx2, abs(a[n-1] - a[n-2]))
    mx = 0
    for j in range(1, n-1):
        temp = abs(a[j] - a[j-1]) + abs(a[j] - a[j+1])
        temp -= abs(a[j-1] - a[j+1])
        mx = max(mx, temp)
    z = tot - mx
    z2 = tot - mx2
    output.append(min(z, z2))

    
print('\n'.join(list(map(str, output))))
