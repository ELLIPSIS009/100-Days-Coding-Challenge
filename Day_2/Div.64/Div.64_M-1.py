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


def cal(da):
    i = 1
    while True:
        b = 64 * i
        db = str(bin(b).replace('0b', ''))
        if len(db) <= len(da):
            counter = 0
            for c in db:
                if c in da:
                    counter += 1
            if counter == len(db):
                return 'yes'
        else:
            return 'no'
        i += 1

a = input()
print(cal(a))