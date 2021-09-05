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