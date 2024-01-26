"""
LAST LESSON EXERCISES
"""

# my_set = set()
#
#
#
# my_values = input("Enter the values: ").split()
#
# my_values = set(my_values)
#
# my_set = my_set.union(my_values)
#
# print(my_set)

# my_set = set(input().split())
#
# print(my_set)
# my_set.clear()
# print(my_set)


# a_set = {'Hello', 2, 0, 56.4, True, False}
# b_set = {'Hola', 1, 56.44, ('Python', 'Django')}
#
# # set_3 = a_set.union(b_set)
#
# a_list = list(a_set)
#
# b_list = list(b_set)
#
# list_3 = a_list + b_list
# set_3 = set(list_3)
#
# print(set_3)

# SET-ler daxilinde list saxlamir.


# my_set = {1, -4, -199.99, 200, 245, 0}
# # Bu set-in minimum elementini tapib onu set-den silen python kodu yazin. (Arasdira bilersiniz)
#
# min_value = min(my_set)
# max_value = max(my_set)
#
# print(min_value)
# print(max_value)

# my_tuple = ("Hello", "Hola", {2, 2, True, 1, False}, ['Hi', 'Everyone', 222], ('Python', 'or', 'C#'))
# # print(my_tuple[2][1])
# # my_tuple[0] = 'Salam'
# my_tuple[4][2] = 'C'
# print(my_tuple[3])

# my_tuple = ('Hola', 'Python', ['Hi', 'Everyone', 'Java'])
# # Java-ni Coding sozu ile evez edin.
#
# my_tuple[2][-1] = 'Coding'
#
# print(my_tuple)

# my_tuple = ('Hola', 'Python', ['Hi', 'Everyone', 'Java'])
# # Python-u Java ile evez edin.
#
# my_list = list(my_tuple)
#
# my_list[1] = 'Java'
#
# my_tuple = tuple(my_list)
#
# print(my_tuple)


# my_variable = 'Salam'
# my_variable2 = ('Salam', )
# # bu 2 deyisen arasindaki ferq nedir ?
#
# print(type(my_variable))
# print(type(my_variable2))


# my_tuple = (-88, 44, 100.0, 11, 111.2, -999)
# # bu tuple-in elementlerini coxdan aza dogru duzun.
# my_list = list(my_tuple)
# my_list.sort(reverse=True)
# my_tuple = tuple(my_list)
# print(my_tuple)


"""
DICTIONARIES -> DICTIONARY
"""
# my_set = set()

# my_dict = {}

# my_dict = {
#     "name": "Intigam",
#     "profession": "Computer Science",
#     "car": "BMW",
# }
#
# print(my_dict)
#
# my_dict['car'] = 'Merc'
#
# print(my_dict)


# my_list = [1,2,3,4,3]
# print(my_list[3])


# my_dict = {
#     "name": "Intigam",
#     "profession": "Computer Science",
#     "car": "BMW",
#     "lesson_days": [2,4,5],
#     "age": 24,
#     "product_price": 254.5
# }
#
# print(my_dict)
# print(type(my_dict))


# my_dict = {
#     "name": "Intigam",
#     "profession": "Computer Science",
#     "car": "BMW",
#     "lesson_days": [2, 4, 5],
#     "age": 24,
#     "product_price": 254.5
# }

# print(len(my_dict)) --> 6

# thisdict = dict(name="John", age=36, country="Norway")
# print(thisdict)


# my_dict = {
#     "name": "Intigam",
#     "profession": "Computer Science",
#     "car": "BMW",
#     "lesson_days": [2, 4, 5],
#     "age": 24,
#     "product_price": 254.5
# }

# print(my_dict["profession"])
# print(my_dict.get('profession'))

# print(my_dict.values())
# print(my_dict.keys())

# print(my_dict.items())

# my_dict = {
#     "name": "Intigam",
#     "profession": "Computer Science",
#     "car": "BMW",
#     "lesson_days": [2, 4, 5],
#     "age": 24,
#     "product_price": 254.5
# }

# my_dict['car'] = 'Merc'
# my_dict.update({"area": "Hovsan"})
#
# print(my_dict)
# my_dict.pop('car')
# print(my_dict)

# my_dict.popitem()
# print(my_dict)

# my_dict = {
#     "name": "Intigam",
#     "profession": "Computer Science",
#     "car": "BMW",
#     "lesson_days": [2, 4, 5],
#     "age": 24,
#     "product_price": 254.5
# }
# # del my_dict['age']
# # my_dict.clear()
# # my_dict2 = my_dict.copy()
# # my_dict2['car'] = 'Hyundai'
#
# print(my_dict)
#
# my_list = [1,2,3]
# my_list2 = my_list.copy()
#
# my_list2[1] = 'Salam'
# print(my_list)


# my_family = {
#     "intigam": {
#         "name" :"Intigam",
#         "surname": "Guluzade",
#         "profession": "Backend"
#     },
#     "fateh": {
#         "name": "Fateh",
#         "age": 11,
#         "profession": "Math",
#     },
# }
# print(my_family['fateh']['age'])


"""
IF, ELIF, ELSE
"""

"""
== --> yoxlayir, beraberdirmi, deyilmi
!= --> beraber deyilse
< --> kicikdir
> --> boyukdur
<= --> kicik beraberdir
>= --> boyuk beraberdir
"""

# a = 5
# b = 5.5

# if a == b:
#     print('Beraberdirler')
# else:
#     print("Beraber deyiller")


"""
Istifadeciden 3 eded alacagiq. Hansi boyukdurse onu cap edeceyik
"""

# num_1 = int(input("Enter first number: ")) # 5
# num_2 = int(input("Enter second number: ")) # 7
# num_3 = int(input("Enter third number: ")) # 3
#
# if num_1 > num_2 and num_1 > num_3:
#     print(num_1 , "boyukdur")
# elif num_2 > num_1 and num_2 > num_3:
#     print(num_2, "boyukdur")
# elif num_3 > num_1 and num_3 > num_2:
#     print(num_3, "boyukdur")

"""
Butun beraber hallar nezere alinsin.
"""

# num_1 = int(input("Enter first number: ")) # -3
# num_2 = int(input("Enter second number: ")) # 3
#
# if num_1 > num_2:
#     if num_2 > 0:
#         print('Ela')
#     else:
#         print('Ikinci Pis')
# else:
#     print('Birinci pis')


# num_1 = int(input("Enter first number: ")) # 3
# num_2 = int(input("Enter second number: ")) # -3

# if not num_1 > num_2: #
#     print('Ela')

# if True:
#     print('Ela')

# if 5 > 3:
#     pass
#
# if 5 > 3:
#     ...


"""
EXERCISES
"""

"""
1. my_dict = {
            "name" :"Intigam",
            "age": 45,
            "profession": "backend",
            }
bu dictionary-nin age hissesinin value-sini 24 ile evez edin.
"""
"""
2.my_dict = {
            "name" :"Intigam",
            "age": 45,
            "profession": "backend",
            "temperature": 38,
            }
Istifadeciden bir eded alin, ve hemin ededin, my_dict-in 
valuelerinde olub olmadigini yoxlayin
"""
# my_dict = {
#             "name" :"Intigam",
#             "age": 45,
#             "profession": "backend",
#             "temperature": 38,
#             }
# a = int(input('Enter value: '))
# if a in my_dict.values():
#     print('Yes')
# else:
#     print('No')
"""
3. my_dict = {
            "ages": [45,56,78,12,23,28],
            "numbers": (56, 24, 12, 34),
            }
key-leri ages ve numbers olan deyerleri birlesdirib, tekrarlari yox edib, tezeden
final key-i ile bu dict-e elave etmek.
"""
my_dict = {
    "ages": [45, 56, 78, 12, 23, 28],
    "numbers": (56, 24, 12, 34),
}

my_list = my_dict["ages"] + list(my_dict['numbers'])
my_set = set(my_list)
my_list = list(my_set)
my_dict['final'] = my_list
print(my_dict)
