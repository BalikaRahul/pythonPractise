given =input('enter your string: ')
given.lower()
vowels=0
Consonants =0
for i  in range(len(given)):
    if given[i] =='a' or given[i] =='e' or given[i] =='i' or given[i] =='o' or given[i] =='u':
        vowels+=1
        
    else:
        Consonants +=1
        
print(f'the number of vowels present in the given is {vowels}')     
print(f'the number of Consonants present in the given is {Consonants}')