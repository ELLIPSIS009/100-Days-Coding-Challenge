# def rotate(l, n):
#     rl = []
#     for i in range(n):
#         temp = []
#         for j in range(n):
#             temp.append(l[n-1-j][i])
#         rl.append(temp)
#     return rl


# n = int(input())
# l = []
# for i in range(n):
#     l.append(list(map(int, input().split(' '))))


# l = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# n = len(l)
# rl = rotate(l, n)
# print(rl)
# for i in rl:
#     print(' '.join(list(map(str, i))))