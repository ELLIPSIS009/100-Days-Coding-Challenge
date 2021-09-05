'''
Question code :- 887A
Platform :- Codeforces
Link :- https://codeforces.com/contest/1446/problem/A

Problem statement :- Top-model Izabella participates in the competition. She wants to impress judges and show her mathematical skills. 
Her problem is following: for given string, consisting of only 0 and 1, tell if it's possible to remove some digits in such a way, 
that remaining number is a representation of some positive integer, divisible by 64, in the binary numerical system.

Example 1:
input : 100010001
output : yes

Example 2:
input : 100
output : no
'''


def cal(a):
    oneFound = False
    zeroCount = 0
    for i in a:
        if oneFound:
            if i == '0':
                zeroCount += 1
        else:
            if i == '1':
                oneFound = True

    if oneFound:
        if zeroCount >= 6:
            return 'yes'
        else:
            return 'no'
    else:
        return 'no'


a = input()
print(cal(a))