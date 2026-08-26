# print all prime number from n to m
# n=int(input('enter the number (start from 2): '))
# m=int(input('enter the range: '))
# for i in range(n,m+1):
#     count =0
#     for j in range(2,m+1):
#         if i%j==0:
#             count+=1
#     if count ==1:
#         print(i,end=' ')
#count to all prime number from m to n 
# n=int(input('enter the number (start from 2): '))
# m=int(input('enter the range: '))
# total=0
# for i in range(n,m+1):
#     count =0
#     for j in range(2,m+1):
#         if i%j==0:
#             count+=1
#     if count ==1:
#         total+=1
# print(f'the total number prime number between{n} and {m} is {total}')


# print all armstrong number in a range  
# n=int(input('enter the starting range : '))
# m=int(input('enter the range: '))
# for i in range(n,m+1):
#     length =len(str(i))
#     num=i
#     total =0
#     while num >0:
#         digit = num%10
#         total+=digit**length
#         num//=10
#     if (total ==i):
#         print(i)

#first prime number from n to m
# n=int(input('enter the number (start from 2): '))
# m=int(input('enter the number: '))
# for i in range(n,m+1):
#     count =0
#     for j in range(2,m+1):
#         if i%j==0:
#             count+=1
#     break
# if count ==1:
#         print(f'The first prime number between {n} and {m} is: {i}')


# last prime from n to m
# n=int(input('enter the number (start from 2): '))
# m=int(input('enter the number: '))
# for i in range(m,n-1,-1):
#     count =0
#     for j in range(2,i):
#         if i%j==0:
#             count+=1
#             break
#     if count ==0:
#         print('the last prime number',i)
#         break

#first vowel in a name 
# name = input('enter your name: ')
# name.lower()
# for i in name:
#     if i == 'a' or i == 'e' or i == 'i' or i =='o' or i =='u':
#         print(f'The first vowel in the name is {i}')
#         break


# last vowel in a name 
# name = input('enter your name: ')
# name.lower()
# for i in range(len(name)-1,-1,-1):
#     if  name[i] == 'a' or name[i] == 'e' or name[i] == 'i' or name[i] =='o' or name[i] =='u':
#         print(f'The first vowel in the name is {name[i]}')
#         break





# print all even number using
# n =int(input('enter the number: '))
# for i in range(n):
#     if i%2==1:
#         continue
#     print(i,end=' ')




# print all odd number using
# n =int(input('enter the number: '))
# for i in range(n):
#     if i%2==0:
#         continue
#     print(i,end=' ')



prime =[]
compsite=[]
n=int(input('enter the number (start from 2): '))
m=int(input('enter the number: '))
for i in range(n,m+1):
    count =0
    for j in range(2,m+1):
        if i%j==0:
            count+=1
    if count ==1:
        prime.append(i)
    else:
        compsite.append(i)
print("prime:", prime)
print("composite",compsite)