# prev_list = [-1,10,-20,2,-90,60,45,20]
# new_list = [number for number in prev_list if number > 0]
# print(new_list)



# prev_list = [-1,10,-20,2,-90,60,45,20]
# sq_neg_list = [number **2 for number in prev_list if number < 0]
# print(sq_neg_list) 






#1

# sentence = "My name is Petar"
# def is_consonant(letter):
#     vowels = "aeiou"
#     return letter.isalpha() and letter.lower() not in vowels

# print(is_consonant("a"))

# consonants = [i for i in sentence if is_consonant(i)]
# print(consonants)



#2

# sentence = "My name is Petar"
# consonants = [letter for letter in sentence if letter.isalpha() and letter not in ["a","e","i","o","u"]]
# print(consonants)






# prev_list = [-1,10,-20,2,-90,60,45,20]
# new_list = [number if number > 0 else 0 for number in prev_list]
# print(new_list)


def get_number(number):
    return number if number > 0 else 0

prev_list = [-1,10,-20,2,-90,60,45,20]
new_list = [get_number(number) for number in prev_list]
print(new_list)