'''
Problem :- Vaccine Production
Platform :- Codechef
Link :- https://www.codechef.com/DEC20B/problems/VACCINE1

Problem statement :- Increasing COVID cases have created panic amongst the people of Chefland, 
    so the government is starting to push for production of a vaccine. 
    It has to report to the media about the exact date when vaccines will be available.
    There are two companies which are producing vaccines for COVID. 
    Company A starts producing vaccines on day D1 and it can produce V1 vaccines per day. 
    Company B starts producing vaccines on day D2 and it can produce V2 vaccines per day. 
    Currently, we are on day 1. We need a total of P vaccines. How many days are required to produce enough vaccines? 
    Formally, find the smallest integer d such that we have enough vaccines at the end of the day d.

Example-1:
Input : 1 2 1 3 14
Output : 3

Example-2:
Input : 5 4 2 10 100
Output : 9
'''


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