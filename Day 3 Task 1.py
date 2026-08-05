name=input('enter the name of the customer: ')
sugar=int(input('enter the price of the rice: '))
palam_oil=int(input('enter the  price of the Palam_oil: '))
egg=int(input('enter the price of the egg: '))
jira=int(input('enter the pirce of the jira: '))
total=sugar+palam_oil+egg+jira
print('the total bill is :' ,total)
print ('discount is in percentage ')
coupon_discount =int(input('enter the coupon: '))
total -=(total *coupon_discount) /100
print('Bill after discount',total)
gst=int(input("Enter the gst percentage: "))
total+=(total*gst)/100
print('bill after adding gst: ', total)
avg = total/4
print('average cost for every item is: ',avg)
no_of_items= int(input('enter the number of items'))
boxes =no_of_items //12
leftOver = no_of_items  % 12
print('no of boxes required is: ', boxes)
print('no of items leftover is: ',leftOver)
storage = boxes ** 2
print('the number of boxes in warehouse is: ',boxes)