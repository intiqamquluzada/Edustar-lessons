"""
SUAL - CAVAB
"""
# mystr = 'salam'
# mystr[0] = 'b'  # STRINGS ARE UNCHANGEABLE
# print(mystr)


# my_list = ['Salam', 'Sagol', 'Necesen']
#
# my_list[0] = 'Hello'
#
# print(my_list)


"""
TUPLES
"""
#
# my_list = ['Salam', 'Hello', 'Hola']
# my_tuple = ('Salam', 'Hello', 'Hola')
#
# print(type(my_list))
# print(type(my_tuple))


# my_tuple = ('Salam',)
# print(type(my_tuple))

# mystr = 'My favourite book is "Sherlock Holmes". '


# my_tuple = ('1', 1, True, False, 2.5)
# print(type(my_tuple))

# my_tuple = ("Hello", "Hola", "World")
#
# my_tuple[0] = 'Salam'
#
# print(my_tuple)

# my_tuple = ("Salam", "Hola", "Hello")
#
# print(my_tuple[2])

# my_tuple = ("Hello", "Hello", "Hola")
# print(my_tuple)

# my_tuple = ("Salam", "Hello")
# print(len(my_tuple))

# my_tuple = ("Salam", "Hello", "Hola", "Nice", "Good")
#
# print(my_tuple[1:4])


# my_tuple = ("Salam", "Hello", "Hola", "Nice", "Good")
# print(my_tuple[-2:-5:-1])


# my_tuple = ("Salam", "Hello", "Hola", "Nice", "Good")
#
# my_list = list(my_tuple)
#
# my_list[1] = 'Bmw'
#
# my_tuple = tuple(my_list)
#
# print(my_tuple)


# my_tuple = ("Salam", "Hello", "Hola", "Nice", "Good")
#
# my_tuple2 = ("Bmw", )
#
# my_tuple = my_tuple + my_tuple2
#
# print(my_tuple)


# my_tuple = ("Salam", "Hello", "Hola", "Nice", "Good")
#
# my_list = list(my_tuple)
#
# my_list.remove('Hola')
#
# my_tuple = tuple(my_list)
#
# print(my_tuple)

# my_tuple = ("Salam", "Hello", "Hola", "Nice", "Good")
#
# del my_tuple
#
# print(my_tuple)


# UNPACKING
# fruits = ("apple", "banana", "cherry")
#
# (green, yellow, red) = fruits
#
# print(green)
# print(yellow)
# print(red)


# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
#
# (green, yellow, *red) = fruits
#
# print(green)
# print(yellow)
# print(red)


# fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
#
# (green, *tropic, red) = fruits
#
# print(green)
# print(tropic)
# print(red)


# tuple1 = ("a", "b" , "c")
# tuple2 = (1, 2, 3)
#
# tuple3 = tuple2 + tuple1
# print(tuple3)

# fruits = ("apple", "banana", "cherry")
# mytuple = fruits * 2
#
# print(mytuple)


# my_tuple = ("BMW", "MERC", "HYUNDAI", "KIA", "BMW")
#
# print(my_tuple.count("BMW"))
# print(my_tuple.index("BMW"))


"""
SETS
"""

# my_set = {"Hello", "Hola", "World", "Hola"}
# # print(type(my_set))
# print(my_set)

# thisset = {"apple", "banana", "cherry", False, True, 0, 1}
#
# print(thisset)
#
# print(len(thisset))

# workers_names = [
#     'Intigam', 'Zaur', 'Mansur', 'Elnur',
#     'Fateh', 'Iltifat', 'Intigam', 'Fateh',
#     'Kenan', 'Natig', 'Zaur'
# ]
#
#
# workers_set = set(workers_names)
#
# workers_names = list(workers_set)
#
# print(workers_names)


# my_set = {'Intigam', 'Guluzade', 'Computer', 'Science'}
#
# my_set.add('ASOIU')
#
# print(my_set)


# thisset = {"apple", "banana", "cherry"}
# tropical = {"pineapple", "tropical", "papaya"}
#
# thisset.update(tropical)
#
# print(thisset)


# thisset = {"apple", "banana", "cherry"}
# mylist = ["kiwi", "orange"]
#
# thisset.update(mylist)
#
# print(thisset)


# my_set = {"Hello", "Hola", "Python", "Django"}
#
# # my_set.remove('Django')
# # my_set.discard("Python")
# # my_set.pop()
# # my_set.clear()
# # del my_set
#
# print(my_set)



# set1 = {"a", "b" , "c"}
# set2 = {1, 2, 3}
#
# set3 = set1.union(set2)
# print(set3)

# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
#
# x.intersection_update(y)
#
# print(x)

# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
#
#
# print(x.intersection(y))

# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
#
# x.symmetric_difference_update(y)
#
# print(x)

# my_list = ['Hello', 'Hola', 'World']
# my_list2 = my_list.copy()
# my_list2[0] = 'Salam'
# print(my_list)


"""
EXERCISES
"""


"""
1. Istifadeciden ededler alin, tekrar olanlari yox edib ekrana cap edin
"""

"""
2. Istifadeciden soz alin ve onun herflerini elifba sirasina gore duzun
"""
# mystr = 'akfn'
# x = sorted(mystr)
# print(x)
"""
3. Istifadeciden 2 ferqli inputda cumleler alin, daha sonra o cumleleri tekrar sozleri yox etmekle
birlesdirin
"""

"""
my_tuple = tuple(('salam'))
ne netice verer --> tuple
"""

"""
my_tuple = ("Salam", "Hello", "WORLD",)
WORLD sozunu Hola sozu ile evez edin
"""

# a = ['a', 'f', 'k', 'n']
#
# my_str = "".join(a) # list-i stringe cevirir
# print(my_str)

# my_tuple = tuple(('salam'))
# print(my_tuple)