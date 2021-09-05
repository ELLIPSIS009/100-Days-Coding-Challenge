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