shoes = int(input('enter the pirce of the shoes: '))
watch = int(input('enter the pirce of the watch: '))
headPhone = int(input('enter the pirce of the headPhone: '))
total =0 
total+= shoes
print('price after adding shoes: ',total)
total+= watch
print('price after adding watch: ',total)
total+= headPhone
print('price after adding headPhone: ',total)
print('discount in percentage')
discount= int(input("enter the discount"))
total-=(total*discount) /100
print("total bill after the discount: ", total)
delivery_charge=(total*5) /100
total +=delivery_charge
print('total bill after adding the delivery charge: ',total)
avg =total // 3
print("split for each is: ", avg)