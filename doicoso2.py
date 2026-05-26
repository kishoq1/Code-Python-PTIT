from math import log2
BASE = '0123456789ABCDEF'
def numberToBase(b, n):
    step = int(log2(b))
    res = ''
    for i in range(0, len(n), step):
        res += BASE[int(n[i:i+step][::-1], 2)]
    return res[::-1]

for r in range(int(input())):
    print(numberToBase(int(input()), input()[::-1]))
