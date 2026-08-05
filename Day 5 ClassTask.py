
age = int(input("enter your age : "))
brith = input("enter your date of birth (yes/no): ")

if age<=3 or brith =='yes' :
    print (f"the is free for you")
elif 4 <= age <=12 :
        print (f" the ticket price for your age groups is 150  ")
elif  13<= age <= 64:
        print (f" the ticket price for your age groups is 250")
elif age <= 64:
        print (f"the ticket price for your age groups is 200")
else:
       print('invalid input')


