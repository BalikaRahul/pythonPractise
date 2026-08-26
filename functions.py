def HypeMan(name,skill):
    return (f"Make some noise for {name}, the absolute master of {skill}!")
name =input('enter  your name: ')
skill = input('enter your skill: ')
print(HypeMan(name,skill))







def check_age(age):
    if 12<=age:
        return (f"Enjoy the ride")
    else:
        return f'Sorry, after {12- age} year you can ride the roller coaster.'
age =int(input('enter your age: '))
print(check_age(age))







def vowel_vacuum(text):
    text=text.lower()
    result =''
    for i in text:
        if i not in 'aeiou':
            result+=i
    return result
text=input('enter your string: ')
print(vowel_vacuum())





def calculate_total(nums):
    total =0
    for i in nums:
        total+=i
    return f'your total today is ${total}'
nums =[2,34,3,2,4,32,89]
print(calculate_total(nums))




def emojify(sentence,mydict):
    for i in mydict:
        sentence=sentence.replace(i,mydict[i])
    return sentence
sentence = input('enter your sentence: ')
mydict = {
    "happy": "😊", 
     "pizza": "🍕", 
     "python": "🐍"
     }
print(emojify(sentence,mydict))





def  print_shopping_list(arr1,arr2):
    Set=set(arr1)
    for i in arr2:
        if i not in Set:
            Set.add(i)
    return list(Set)
arr1=["flour", "sugar", "eggs"]
arr2 = ["eggs", "butter", "sugar", "vanilla"]
print(print_shopping_list(arr1,arr2))




def check_anagrams(word1,word2):
    arr = list(word1.lower().replace(" ", ""))
    arr2 = list(word2.lower().replace(" ", ""))
    dict1 ={}
    dict2 = {}
    for i in arr:
        if i not in dict1:
            dict1[i]=1
        else:
            dict1[i]+=1
    for i in arr2:
        if i not in dict2:
            dict2[i]=1
        else:
            dict2[i]+=1
    if dict1==dict2:
        return "Yes, those are anagrams!"
    else:
        return "no, those are not anagrams!"
word1="Clint Eastwood"
word2="Old West Action"
print(check_anagrams(word1,word2))

        
