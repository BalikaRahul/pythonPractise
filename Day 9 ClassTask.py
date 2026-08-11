menu_items = ['Burger','pizza','pasta','fries','coke']
menu_price = [120,250,180,90,50]
for i in range(len(menu_items)):
    print(i+1, menu_items[i], '--', menu_price[i])
print('='*80)
ordered_items=[]
ordered_prices=[]
users=['kaushik','pavan','ram','harish','rajesh','ravi','raju']
user=input('enter your name: ')
print('='*80)
user.lower()
print('enter "exit" or "done" after ordering the food ')
while True:

    item =input("enter the item number: ")
    if item == 'exit' or item =='done' :
        print('='*80)
        for i in range(len(ordered_items)):
            print(i+1, ordered_items[i], ordered_prices[i])
        break
    Item=int(item)
    if menu_items[Item] in menu_items:
        ordered_items.append(menu_items[Item])
        ordered_prices.append(menu_price[Item])
    else:
        print(f"the item you enter is not avaliable right now: {item}")
total=0
for i in range(len(ordered_prices)):
    total+=ordered_prices[i]
print('='*80)
print(f'The total order value is :{total}')
print('='*80)
print('discount for new customer is welcome100')
print('discount for old customer is save10')
discount=input('enter the coupon: ')
if user in users and discount == 'welcome100':
    print(f'sorry {user} you are not eligible to use this coupon')
elif user not in users and discount == 'welcome100':
    total-=50
elif discount == 'save10':
    total-=(total*10)//100
else:
    print(f'iinvalid coupon {discount}')
print('='*80)
print(f'Total cost of the order afer the discount is {total}')
print('='*80)
gst=18
total+=(total*gst)//100
print(f'The grand Total of the order is {total}')    
