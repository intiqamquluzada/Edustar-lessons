# print('''Today is our second lesson
#     Let's go''')


# print('salam', end='---')
# print('sagol')


# x = input('Enter value: ')  # '140'
#
# print(type(x))  # <class: str>
#
# x = int(x)
#
# print(type(x))  # <class: int>

# print(x % 2)
#
# print(54 // 4)  # 13
# print(54 / 4)  # 13.5
# print(3 ** 2)  # 9


"""

                                  STRINGS

"""

# print(type('Hello'))

# my_variable = '''
# salam
# necesiz?
# salam
# salam
# '''
# print(my_variable)


# CASTING

# name = 'Intigam'

# print(name[1:6:2])
# print(name[2:])
# print(name[-3::1])

# print(len(name))

# word = input("Enter the word: ")

# print(word[-1])

# print(word[len(word)-1])

# word = 'Python is the Best'

# print(word.upper()) --> Butun herfleri boyudur
# print(word.lower()) --> Butun herfleri kicildir
#
# my_word = '  Hello World  '
#
# print(my_word.strip()) # butun bosluqlari silir

# my_word = 'Salam bugun hava yaxsi kececek'
# my_list = my_word.split() # str-i icine verdiyimiz deyere gore ayirib list-e cevirir
# print(my_list)


# word_1 = 'Salam'
# word_2 = 'Sagol'
#
# print(word_1 + " " + word_2) # str-lerde + emeli onlari birlesdirir


# age = 36
# text = 'My age is ' + str(age)
# print(text)



# age = 36
#
# text = 'My age is {}'
#
# print(text.format(age))

# age = 36
#
# text = f"My age is {age}"
#
# print(text)


# quantity = 3
# itemno = 567
# price = 49.95
# myorder = "I want {} pieces of item {} for {} dollars."
# print(myorder.format(quantity, itemno, price))

# text = 'My favourite book is "Sherlock Holmes" '
# print(text)


# txt = "We are the so-called \"Vikings\" from the north."
# print(txt)



# my_word = 'SAlam Dersbasladi'


# print(my_word.capitalize()) # str-in ilk herfini boyudur

# print(my_word.casefold()) # butun herfleri kicildir

# print(my_word.center(50))# reqemi goturub ikiye bolub sagdan ve soldan merkezleyir

# print(my_word.count('A'))

# print(my_word.endswith('adi')) # sozun bitdiyi hisseni yoxlayir ve True yada False qaytarir

# print(my_word.find("s")) # simvolun indeksini tapib , qaytarir

# print(my_word.index('i')) # simvolun indeksini qaytarir

# my_value = input('Enter the value: ')  # '777'
#
# print(my_value.isdigit()) # tipin edede cevrilib cevrile bilmeyecyini teyin edir, True ve False

# my_word = 'SAlam ders basladi'

# print(my_word.startswith('SA')) # ne ile basladigini yoxlayir, True ve False

# print(my_word.title())



"""

                                      BOOLEANS


"""

# print(7 > 2)
# print(7 < 2)
# print(7 == 2)
# print(7 >= 2)
# print(7 <= 2)


# number_1 = input('Enter the first number') # 8
# number_2 = input('Enter the second number') # 2
#
# if number_1 > number_2:
#     print(number_1)
# else:
#     print(number_2)


# Istifadeciden eded alacagiq, ededin tek yaxud cut oldugunu tapan kod
# EDILDI

# Istifadeci soz daxil edir, bu sozun uzunlugunun tek yaxud cut oldugunu tapan kod
# EDILDI

# Istifadeci bankomat kartina sifre qoymalidir. Sifrenin uzunlugu 4 olmalidir
# dogru oldugu halda qebul edildi cap olunsun,
# eks halda
# uzunluq 4-e beraber olmalidir cap olunsun.
# Hemcinin sifre reqemlerden ibaret olmalidir
# herf olmaz , eks halda herf olmaz cap olunsun.


# password = input('Enter the password: ')

# if len(password) == 4:
#     print('Accepted')
#     if password.isdigit():
#         print('Accepted')
#     else:
#         print("Not accepted")
# else:
#     print('Password length is not enough')

# if len(password) == 4 and password.isdigit():
#     print('Accepted')
# else:
#     print('Not accepted')


"""

AND, OR

"""

# OR --> eger en az bir dene True varsa netice True-dir

# x = 7 > 9 or 9 > 8
# print(x)

# AND --> her biri True olmalidir ki, neticede True olsun
# y = 7 > 9 and 9 >8
# print(y)


# Istifadeci adini ve soyadini 2 ayri inputda daxil edecek
# onun adini ve soyadini birlesdirib birdene mail duzeldib
# capa vermek


# name = input('Enter the name: ')
# surname = input('Enter the surname: ')
# end_mail = '@gmail.com'
# user_email = name + surname + end_mail
# print(user_email)

# Daxil edilmis sozun uzunlugu tekdirse ortadaki herfi
# Daxil edilmis sozun uzunlugu cutdurse ortadaki 2 herfi
# cap etmek


# word = input('Enter the word')
#
# if len(word) % 2 == 0:
#     print(word[len(word)//2-1: len(word)//2 + 1]) # defter
# else:
#     print(word[len(word)//2])


# Istifadeciden cumle aliriq, hemin cumlede nece eded @ isaresi oldugunu tapiriq
# EDILDI




