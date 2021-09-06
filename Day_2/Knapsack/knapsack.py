'''
Question code :- A. Knapsack
Link :- https://codeforces.com/contest/1446/problem/A

Problem statement :- You have a knapsack with the capacity of W. There are also n items, the i-th one has weight wi.
You want to put some of these items into the knapsack in such a way that their total weight C is at least half of its size, 
but (obviously) does not exceed it. Formally, C should satisfy: ⌈W2⌉≤C≤W.
Output the list of items you will put into the knapsack or determine that fulfilling the conditions is impossible.
If there are several possible lists of items satisfying the conditions, you can output any. 
Note that you don't have to maximize the sum of weights of items in the knapsack.

Example :

input
3
1 3
3
6 2
19 8 19 69 9 4
7 12
1 1 1 17 1 1 1

output
1
1
-1
6
1 2 3 5 6 7
'''

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