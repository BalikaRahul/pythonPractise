Days =int(input("enter the number of day: "))
cal=1
for i in range(1,Days+1):
    cal*=2
    print(f'Day {i} = {cal}')