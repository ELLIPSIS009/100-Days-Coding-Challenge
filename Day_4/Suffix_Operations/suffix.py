'''
Problem :- Suffix Operations
Platform :- Codeforces
Link :- https://codeforces.com/contest/1453/problem/B

Problem statement :- Gildong has an interesting machine that has an array a with n integers. 
    The machine supports two kinds of operations:
        1. Increase all elements of a suffix of the array by 1.
        2. Decrease all elements of a suffix of the array by 1.
    A suffix is a subsegment (contiguous elements) of the array that contains an. 
    In other words, for all i where ai is included in the subsegment, all aj's where i<j≤n must also be included in the subsegment. 
    Gildong wants to make all elements of a equal — he will always do so using the minimum number of operations necessary. 
    To make his life even easier, before Gildong starts using the machine, you have the option of changing one of the integers in the array to any other integer. 
    You are allowed to leave the array unchanged. You want to minimize the number of operations Gildong performs. 
    With your help, what is the minimum number of operations Gildong will perform? Note that even if you change one of the integers in the array, 
    you should not count that as one of the operations because Gildong did not perform it.

Example : 

input : 
7
2
1 1
3
-1 0 2
4
99 96 97 95
4
-3 -5 -2 1
6
1 4 3 2 4 1
5
5 0 0 0 5
9
-367741579 319422997 -415264583 -125558838 -300860379 420848004 294512916 -383235489 425814447

output : 
0
1
3
4
6
5
2847372102
'''


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
