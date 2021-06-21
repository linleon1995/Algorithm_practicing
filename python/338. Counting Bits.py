"""
Leetcode
338. Counting Bits
Easy.
"""

# 1
def fun1(n):
    bits = [0]
    cnt = 0
    if n == 0:
        return bits
    for i in range(1, n+1):
        num = i
        cnt = 0
        while num != 0:
            cnt += num%2
            num //= 2
        bits.append(cnt)
    return bits

# 2
def fun2(n):
    bits = [0]
    cnt = 0
    base = []
    if n == 0:
        return bits
    for i in range(1, n+1):
        num = i
        cnt = 0
        if math.log(i,2) == float(int(math.log(i,2))):
            base.append(i)
            cnt = 1
        else:
            j = len(base) - 1
            while j >= 0:
                if num >= base[j]:
                    num -= base[j]
                    cnt += 1
                j -= 1
        bits.append(cnt)
    return bits
    
    
# 3
def func3(n):
    res = [0] * (n + 1)
    for i in range(n + 1):
        res[i] = res[i >> 1] + (i & 1)
    return res