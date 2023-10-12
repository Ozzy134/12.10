def season(a):
    if (a <= 2 and a != 12):
        print('Зима')
    elif (a <= 5):
        print('Весна')
    elif (a <= 8):
        print('Лето')
    else:
        print('Осень')

a = int(input())
print(season(a))
