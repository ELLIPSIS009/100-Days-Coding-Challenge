d1, v1, d2, v2, p = list(map(int, input().split(' ')))

sum = 0
days = 0
for i in range(1, max(d1, d2)+1):
    if sum >= p:
        break
    if i >= d1:
        sum += v1
    if i >= d2:
        sum += v2
    days += 1

while sum < p:
    days += 1
    sum += (v1 + v2)

print(days)