size = input('enter your size: ')
milk= input('enter your choice of milk: ')
espresso= bool(input("Enter True or False: "))
total = 0 
if size == 'small':
    total+=180
    if milk == 'standard':
        total+=0
    else:
        total+=45
        if espresso== True:
            total+=90
        else:
            total+=0
elif size == 'medium':
    total+=240
    if milk == 'standard':
        total+=0
    else:
        total+=45
        if espresso== True:
            total+=90
        else:
            total+=0
    
else:
    total+=240
    if milk == 'standard':
            total+=0
    else:
        total+=60
        if espresso== True:
            total+=90
        else:
            total+=0
print(total)
