def Count(String):
    String =String.lower()
    vowel =0
    space =0
    consonants =0
    digit =0
    for i in range(len(String)):
        if String[i] in 'aieou':
            vowel+=1
        elif String[i] in '0123456789':
            digit+=1
        elif String[i] ==' ':
            space+=1
        else:
            consonants+=1
    return f'space{space} vowels{vowel} digits{digit} consonants{consonants}'
print(Count(String="python 123"))
