"""

LAST LESSON EXERCISES

"""

# my_dict = {
#     "name" :"Intigam",
#     "age": 45,
#     "profession": "backend",
#     "temperature": 38,
# }
# a = input()
# # b = input()
#
# if a in my_dict.keys():
#     print("Bele key artiq movcuddur")
# else:
#     my_dict[a] = 'test'
#
# print(my_dict)

# -------------------------------------------------------------

# num_1 = int(input("Enter first number: "))  # 7
# num_2 = int(input("Enter second number: "))  # 7
# num_3 = int(input("Enter third number: "))  # 3
#
# if num_1 > num_2 and num_1 > num_3:
#     print(num_1, "boyukdur")
# elif num_2 > num_1 and num_2 > num_3:
#     print(num_2, "boyukdur")
# elif num_3 > num_1 and num_3 > num_2:
#     print(num_3, "boyukdur")
# elif num_1 == num_2 > num_3:
#     print(num_1 and num_2, "boyukdur")
# elif num_1 == num_3 > num_2:
#     print(num_1 and num_3, "boyukdur")


# ---------------------------------------------------------------

# sentence = input()
# k = len(sentence)
# my_list = sentence.split() # ['salam', 'necesiz']
# length_list = len(my_list) # 2
# print(k - (length_list-1))


# ------------------------------------------------------------------

# 4. Daxil edilen herfin sait yaxud samit oldugunu tapan python kodu yazin.

# saitler = ['a', 'i', 'e', 'o', 'ö', 'ü', 'ı', 'ə', 'u']
#
# herf = input('Enter the alpha: ')
#
# if herf in saitler:
#     print('Saitdir')
# else:
#     print('Samitdir')

# ------------------------------------------------------------------

# a = input().split()
# a.sort()
# # x = sorted(a) # stringi cevirir list-e, sonra sort edir, list kimi qaytarir
# print(a)

# -- True form --
# a = input('Enter 7 numbers: ').split()
# print(a)
# a = list(map(int, a))
# a.sort()
# print(a)
# -------------------------------------

# a = input('Enter the word: ') # lapal
#
# print(a) # lapal
#
# reverse_a = a[::-1] # lapal
#
# if a == reverse_a:
#     print('Beraberdir')
# else:
#     print('beraber deyil')


# ------------------------------------------------------

# 7. Polindrom eded o edede deyilir ki, tersi ile ozu birbirine beraber olsun.
# Meselen, 77, 121, 212 ve s.
# Daxil edilen ededin polindrom olub olmadigini yoxlayan python kodu yazin.
# --DONE

# ------------------------------------------------------

# 8. my_list = [[1,2,3], [4,5,6], [7,8,9]] metodlardan istifade ederek bu list-i
# my_list = [[9,8,7], [6,5,4], [3,2,1]] veziyyetine getirin.

# my_list = [[9,8,7], [6,5,4], [3,2,1]]

# my_list = [[4,5,6], [2,1,3], [7,8,9]]
#
# my_list.sort() #  [2,1,3],[4,5,6],[7,8,9]
# my_list[0].sort() # [1,2,3], [4,5,6], [7,8,9]
# my_list[1].sort()
# my_list[2].sort()
# print(my_list)

# ----------------------------------------
# website_passwords = {
#     "intigam": {
#         "password": "salamsalam1234@"
#     },
#     "kenan": {
#         "password": "s@l@m1234"
#     },
#     "resul": {
#         "password": "python&django"
#     },
#     "fateh": {
#         "password": "monday$$python"
#     },
#     # "cavidan": {
#     #     "password": ...
#     # }
# }
#
# passwd = input('Enter your password: ')
#
# if len(passwd) > 8 and not passwd.isdigit():
#     website_passwords.update({"cavidan": {"password": passwd}})

# print(website_passwords)

# -------------------------------------------------------------
# 10. Istifadeciden bir eded alin
# ve onun son reqeminin tek yoxsa cut oldugunu tapan python kodu yazin.

# a = input('Enter the number: ')
#
# last_digit = a[-1]
#
# last_digit = int(last_digit)
#
# if last_digit % 2 == 0:
#     print('Cut')
# else:
#     print('tek')

"""
END EXERCISES
"""

"""
                                    WHILE
"""

# number = 1
#
# while number <= 10:
#     print(number)
#     number = number + 2

# i = 0
#
# while i < 10:
#     i += 1
#     if i == 3:
#         continue
#
#     print(i)


# i = 0
#
# while i < 10:
#     i += 1
#     if i % 2 == 0:
#         continue
#     print(i)


# i = 10
#
# while i > 0:
#     i -= 1
#     print(i)

# while True:
#     print('SAAAAALAAAM')


# my_list = ['python', 'django', 'flask', 'fastapi']
#
# i = 0
#
# while i < len(my_list):
#     print(my_list[i])
#     i += 1

"""
Istifadeciden 2 eded alin, hemin ededler arasinda olan
ededleri cap edin.
"""

# a = int(input('Enter first number: '))  # 45
# b = int(input('Enter second number: '))  # 75
#
# i = a
#
# while i < b:
#     i += 1
#     print(i)

"""
Istifadeci daxil etdiyi sozun butun herflerini cap edin. 
"""
#
# word = input('Enter the word: ')
# i = 0
#
# while i < len(word):
#     print(word[i])
#     i += 1

"""
Istifadecinin daxil etdiyi ededdden 100e qeder olan ededleri cap edin.
"""
