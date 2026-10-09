n =7
# for i in range (n,-1,-1):
#     for k in range(n-i-1):
#         print(" ",end=' ')
#     for j in range(2*i+1):
#         if j==0 or j==2*i or i == n-1 :
#             print(i,end=' ')
#         else:
#             print(" " ,end =' ')
#     print()
# for i in range(n):
#     for k in range(n-i-1):
#         print(' ',end =' ')
#     for j in range(2*i+1):
#         if j ==0 or j==2*i  :
#             print("*",end=' ')
#         else:
#             print(" ",end=' ')
#     print()
for i in range(n-1,-1,-1):
    for k in range(n-i-1):
        print(' ',end =' ')
    for j in range(2*i+1):
        if j ==0 or j==2*i  :
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()

