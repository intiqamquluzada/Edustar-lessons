"""
LAST LESSON EXERCISES
"""

# a = int(input())
# i = a
# while i < 50:
#     i += 1
#     if i % 2 == 0:
#         continue
#     print(i)


# ----------------------------------
# 3. my_list = [1,2,3,4,5] , new_list = []
# my_list-in elementlerinden cut olanlari new_list-e elave edin.

# my_list = [1, 2, 3, 4, 5]
# new_list = []
#
# i = 0
# while i < len(my_list):
#     if my_list[i] % 2 == 0: # my_list -> [1,2,3,4,5], my_list[0] -> 1, my_list[1] -> 2
#         new_list.append(my_list[i])
#     i += 1
# print(new_list)


# i = 0
#
# while i < 10:
#     print(i)
#     my_list[i]
#     i += 1


# ---------------------------------------------------------------

# my_list = ['python', 'django', 'java', 'springboot'] , new_list = []
# my_list-in elementlerini new_list-e elave edin, amma java elave edilmesin

# my_list = ['python', 'django', 'java', 'springboot']
# new_list = []


# print(len(my_list))
# i = 0
# while i < len(my_list):
#     if my_list[i] == 'java':
#         i += 1
#         continue
#     new_list.append(my_list[i])
#     i += 1

# -------------------------------------------------------------

# 5. my_tuple = ('salam', '222', '22.5', 'new', 's23', 'a.5')
# Numerice tip- e cevrile bilen elementleri yeni bir list-e elave edin.

# my_tuple = ('salam', '222', '22.5', 'new', 's23', 'a.5')
# new_list = []
# .isdigit()

# i = 0
# while i < len(my_tuple):
#     if my_tuple[i].isdigit():
#         new_list.append(my_tuple[i])
#
#     i += 1
#
# print(new_list)


# - ----------------------------------------


# 1-den 100-e qeder olan ededlerin icerisinden 10,20,... olanlari cap edin.

# i = 0
# while i < 100:
#     i += 1  # (i+=10)
#     if i % 10 == 0:
#         print(i)


# i = 0
# while i < 101:
#
#     print(i)
#     i += 10


# - --------------------------------


# 7. Istifadeciden cumle alin, hemin cumlede i herfinin sayini tapin.


# count_i = 0
# sentence = input("Enter the sentence: ")
# i = 0
# while i < len(sentence):
#     if sentence[i] == 'i':
#         count_i += 1
#     i += 1
# print(count_i)

# ---------------------------------------------------------------------
# While dovr operatoru ile my_list = ['1', '2', '3', '4', '5', '6']
# bu list-in her bir elementini int- tipe cevirin.
# my_list = ['1', '2', '3', '4', '5', '6']

# i = 0
# while i < len(my_list):
#     my_list[i] = int(my_list[i])
#     i += 1
# print(my_list)

# -------------------------------------------------------------------



# 9. my_list = [1,2,3,4,5,67,65,43]
# bu list-in elementlerinin cemini tapin.

# my_list = [1,2,3,4,5,67,65,43]
# sum_of_numbers = 0
# i = 0
# while i < len(my_list):
#     sum_of_numbers += my_list[i]
#
#     i+= 1
#
# print(sum_of_numbers)

#-----------------------------------------------------------------------
# Istifadeciden 1 inputda ededler alib, list-e yigin.
# Daha sonra hemin list-deki elementlerin cemini tapin.


# my_numbers = input('Enter the numbers: ')
# sum_of_numbers = 0
#
# my_numbers = my_numbers.split() # ['3','4','5','6','7']
#
# i = 0
# while i < len(my_numbers):
#     sum_of_numbers += int(my_numbers[i])
#     i += 1
# print(sum_of_numbers)


#-----------------------------------------------

# i = 1
# while i < 11:
#     if i == 3:
#         break
#     print(i)
#     i += 1

# ---------------------------------------------

# print(True or False and False or True and False) # True or False or False --> True

















