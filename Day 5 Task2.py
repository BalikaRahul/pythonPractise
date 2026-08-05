character = input("enter your character: ")
action = input('enter your action: ')
if character=='knight' and action==' attack':
    print("Your sword pierces the dragon's scales! Victory!")
elif character == 'mage' and action =='cast spell':
    print(" A surge of frost freezes the dragon solid! Victory! ")
elif character == 'rouge' and action == 'flee':
    print("You vanish into the shadows and escape safely!")
elif action == 'flee' :
    print("You're too slow! The dragon catches you! ")
else:
    print("Your attack misses, and the dragon breathes fire! Game Over!")