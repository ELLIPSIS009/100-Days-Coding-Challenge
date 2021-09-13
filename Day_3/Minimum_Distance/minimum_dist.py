'''
Problem :- Minimum Distances
Platform :- HackerRank
Link :- https://www.hackerrank.com/challenges/minimum-distances/problem

Problem statement :- The distance between two array values is the number of indices between them. 
Given a , find the minimum distance between any pair of equal elements in the array. 
If no such value exists, return -1.

Example :

Sample Input
STDIN           Function
-----           --------
6               arr[] size n = 6
7 1 3 4 1 7     arr = [7, 1, 3, 4, 1, 7]

Sample Output
3
'''


l = int(input())
arr = list(map(int, input().split(' ')))
dist = []

for i in range(l):
    for j in range(i+1, l):
        if arr[i] == arr[j]:
            dist.append(abs(j-i))

if len(dist) == 0:
    print(-1)
else:
    print(min(dist))