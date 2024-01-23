# c = input()  # 43534a
#
# if len(c) == 5 and c.isdigit():
#     print("Congratulations")
# else:
#     print("failed")  # int(input() yazib birinci yazilani etmek istedim error verdi


# number = int(input("Enter the number: "))
#
# print(len(number))


"""

12. Daxil edilen sozun uzunlugu cut ededdirse onda onun ortadaki 2 herfini,
 eger uzunlugu tek ededdirse tam ortadaki herfini ekrana cap eden python kodu yazin.

"""

# word = input('Enter the word: ') # salam, defter
#
# word_length = len(word) # 5,  6
#
# # defter --> defter[2], defter[3]
#
# if word_length % 2 == 0:
#     print(word[word_length//2-1], word[word_length//2])
# else:
#     print(word[word_length//2])


"""

INT, FLOAT, COMPLEX

"""

# print(type(8))
#
# print(type(8.0))
#
# print(type(5j))


# my_value = float(input("Enter the number: "))
# print(my_value)

# my_number = 9
# print(float(my_number))




"""
LISTS
"""

# my_list = [1, True, 'Salam', 2.0, 'Salam', True] # isleme sureti tuple-lara nezeren zeifdir.
# # print(my_list)
# print(my_list)
# my_list[2] = 4
# print(my_list)



"""
1. Siralidir (Ordered) --> indeksle cata bilirik
2. Tekrar qebul edir (Allow duplicates)
3. Deyiskendirler (Changeable)
"""


# my_list = ['Intigam', 'Guluzade', 'Python', 'Django']

# print(len(my_list))

# print(my_list[0][1])


# my_list[2:4] = ['salam', 'sagol']
#
# print(my_list)

# age = int(input("Enter your age: ")) # 12
#
# ages_list = [10,11,12,13,14,15,16,17,18,19,20]

# if age in ages_list:
#     print('You can login')
# else:
#     print("you dont have access")




# thislist = ["apple", "banana", "cherry"]
# thislist.insert(2, "watermelon")
# print(thislist)



# thislist = ["apple", "banana", "cherry"]
#
# thislist.append("orange")
#
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# # thislist.extend(tropical)
# # print(thislist)
# print(thislist + tropical)


# my_list = ['Python', 'Django', "FastAPI", "Flask", "Kiwi"]
#
# my_list.remove('Flask')
#
# print(my_list)


# my_list = ['Python', 'Django', "FastAPI", "Flask", "Kiwi"]


# my_deleted_value = my_list.pop(2)
#
# print(my_deleted_value)
# print(my_list)


# del my_list[1]
# print(my_list)

# del my_list
# print(my_list)



# my_list = ['Python', 'Django', "FastAPI", "Flask", "Kiwi"]
#
# my_list.clear()
#
# print(my_list)


# numbers_list = [34, -7, 45, 223, 1212, -77, 0, 100]
#
# numbers_list.sort(reverse=True) # coxdan aza dogru siralayir
# numbers_list.sort()
#
# print(numbers_list)


# my_list = ['alma', 'armud', 'nar', 'ciyelek']
#
# my_list.sort()
#
# print(my_list)


# my_list = ['Salam', "Hello", 'Sagol', 'GoodBye']
# my_list.reverse() # tersine siralayir
# print(my_list)


# my_list = ['alma', 'armud', 'nar']
#
# my_list_2 = my_list.copy()
#
# my_list_2[0] = 'alca'
#
# print(my_list_2)
# print(my_list)

# my_sentence = input("Enter the sentence: ").split("-")
#
# print(my_sentence)


"""
EXERCISES
"""

"""
Istifadeciden cumle alacagiq, daha sonra o cumlede sozleri elifba sirasina gore siralayacagiq
"""
"""
Istifadeci inputda bosluqla ededler daxil edir, daha sonra onlari coxdan aza dogru siralayib, 
ekrana cap edin
"""
"""
Istifadeci 2 ayri cumle daxil edecek, hemin cumleleri aralarinda vergul isaresi ile birlesdirib
ekrana cap edin
"""
"""
Listden silinen elementi yeni liste elave eden python kodu yazin.
"""
"""
my_list = [23, 45, 43, 42, 30, 12] -> sort-dan istifade edin
List-in en boyuk ededi ile en kicik ededinin cemini ekrana cap edin
"""
"""
Daxil edilen sozun 2ci indeksini basqa herfle evez eden python kodu yazin.
ARASDIRMA
"""
"""
Daxil edilen 3 eded sozu
avtomatik olaraq
my_list = ['salam','sagol', 'hello','goodbye', 'nice', 'good']
sagol, hello, goodbye sozlerinin yerine yerlesdirin.
"""

# Input: bmw mercedes hyundai
# Output: ['salam','bmw', 'mercedes','hyundai', 'nice', 'good']


# my_list = ['salam','sagol', 'hello','goodbye', 'nice', 'good']
#
# words = input("Enter three words: ").split()
# my_list[1:4] = words
# print(my_list)


#
# a = ['salam', 'sagol']
# a[2] = 'b'
# print(a)



