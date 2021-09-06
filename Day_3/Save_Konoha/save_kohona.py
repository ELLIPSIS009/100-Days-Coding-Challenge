count = int(input())
for i in range(count):
    n, z = list(map(int, input().split(' ')))
    a = list(map(int, input().split(' ')))
    counter = 0
    while z > 0:
        attack = max(a)
        z -= attack
        a[a.index(attack)] = a[a.index(attack)] / 2
        counter += 1
if counter == 0:
    print('Evacuate')
else:
    print(counter)