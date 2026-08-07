# Task 1
n =int(input('enter the number: '))
count =0
i=1
while i<n+1:
    if n%i==0:
        count+= 1
    i+=1
if count==2:
    print("it is a prime number")
else:
    print('not a prime number')
# Task 2 using recursion
def fib(n):
    if n<=1:
        return n
    return fib(n-1)+fib(n-2)
n=int(input('enter the number: '))
result = fib(n)
print(result)
# without function
n=int(input('enter the number: '))
a=0
b=1
for i in range(1,n+1):
    print(a,end=' ')
    c=a+b
    a=b
    b=c
# Task 4
while True:
    num = int(input('enter the number: '))
    if num == 3:
        print(f'you have guessed the number :{num}')
        break
    elif num >3:
        print('the number is lower than your guess  ')
    elif num< 3:
        print('the number is higher than your guess ')
    else:
        print('wrong guess')
