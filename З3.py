def power(a, n):
    res = 1
    if n > 0:
        for i in range(n):
            res *= a
        return res
    elif n < 0:
        for i in range(-n):
            res /= a
        return res
    return res

print(power(int(input()), int(input())))