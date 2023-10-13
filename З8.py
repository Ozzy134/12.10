def s_prime(x):
    for i in range(2, (x//2)+1):
        if x % i == 0:
            return 'Ложь'
    return 'Правда'

x = int(input())
print(s_prime(x))