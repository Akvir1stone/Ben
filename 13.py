def ret(s):
    r200 = s // 200
    s = s % 200
    r100 = s // 100
    s = s % 100
    r25 = s // 25
    s = s % 25
    r10 = s // 10
    s = s % 10
    r5 = s // 5
    s = s % 5
    r1 = s
    return f'{r200} - 2$; {r100} - 1$; {r25} - 25 cents; {r10} - 10 cents; {r5} - 5 cents; {r1} - 1 cents'


print(ret(2346))
