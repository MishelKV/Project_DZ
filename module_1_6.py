my_dict={'Vasya': 1975, 'Egor': 1999, 'Masha': 2002}
print(my_dict)
print(my_dict.get('Vasya'))
print(my_dict.get('Mikhail'))
print(my_dict.get('Mikhail','Нет такого имени!'))
my_dict.update({"Sasha" : 1976, "Alex":1980})
a = my_dict.pop("Egor")
print(a)
print(my_dict)

my_set={1, 'Яблоко', 1, 'Яблоко',  42.314}
print(my_set)
print(my_set.add(13))
print(my_set.add((5, 6, 1.6)))
print(my_set.discard(1))
print(my_set)

