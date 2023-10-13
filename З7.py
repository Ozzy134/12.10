def bank(a,time):
    for each_year in range(time):
        a = (a * 1.1)
    return a

a = int(input())

time = int(input())

print(bank(a,time))