# items=[]
# prices=[]
# while True:
#     item  = input('enter the item: ')
#     if item == 'exit' :
#         for i in range(len(items)):
#             print(i+1, items[i], prices[i])
#         break
#     price = int(input('enter the price of the item: '))
#     items.append(item)
#     prices.append(price)
# Total=sum(prices)
# print('Total: ',Total)
# gst=18
# Total+=(Total*gst)//100
# print("grandTotal: ",Total)
n=int(input('enter the height: '))
for i in range(n):
    for space in range(n-i-1):
        print(" ",end=' ')
    for j in range(2*i+1):
        print('*',end=' ')
    print()
for i in range(n-1):
    for space in range(i+1):
        print(' ',end=' ')
    for j in range(2*(n-i-1)-1):
        print('*',end=' ')   
    print()
