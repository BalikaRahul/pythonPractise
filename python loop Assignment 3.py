#Task 1
members = int(input("enter the members: "))
cars =0
cars =members//5
extra = members%5
cars+=extra
print(f'the total cars required is : {cars}')

# Task 2
arr = [1,2,6,4]
sec=0
largest =0
for i in range(len(arr)):
    if arr[i]>largest:
        sec =largest
        largest=arr[i]
    elif largest >arr[i]>sec:#checking whether the last element is second largest number in the array
        sec=arr[i]
print(sec)

#Task 3 
year = int(input('enter the year: '))
if year%400==0 or (year%4==0 and year%100!=0):
    print(f'the given year is a leap: {year}')
else:
    print(f'the given year is not a leap year: {year}')
#Task 4
n = int(input('enter the number of row to be print: '))
for i in range(n):
    for j in range(n-i):
        print("*",end=' ')
    print()