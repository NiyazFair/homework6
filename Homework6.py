my_dict = {'Niyaz': 1988, 'Irek': 1981}
print(my_dict)
print(my_dict['Niyaz'])
print(my_dict.get('Roza'))
my_dict.update({'Roza': 55,
                'Rail': 37})
a = my_dict.pop('Irek')
print(a)
print(my_dict)
my_set = {1, 2, 3, 1, 2, 3, 'Fruit', 15.17}
print(my_set)
my_set.update({4, 5})
print(my_set)
my_set.remove(1)
print(my_set)
