total_height=int(input("enter the height: "))
for i in range(total_height):
    total_height+=i
    print("Total: ",total_height)
# Task2
interval = int(input('enter the time'))
for i in range(1,interval+1,2):
    print('Alarm ringing at minute: ', i)
# Task 3
Days =int(input("enter the number of day:10 "))
cal=1
for i in range(1,Days+1):
    cal*=2
    print(f'Day {i} = {cal}')
# Task 4
n = int(input('enter the number: '))
for i in range(1,n+1):
    if i%3==0 and i%5==0:
        print("POP!")
    elif i %3==0:
        print('Sanp!')
    elif i%5==0:
        print('Crackle')
    else:
        print(i)