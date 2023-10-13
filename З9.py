def date(a, b, c):
    if a <= 31 and b <= 12 and c <= 2023:
            return 'Такое число может быть'
    return 'Такого числа не может быть'

a = int(input())
b = int(input())
c = int(input())
print(date(a, b, c))