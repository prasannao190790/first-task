Python 3.11.6 (tags/v3.11.6:8b6ee5b, Oct  2 2023, 14:57:12) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #creating a list
>>> my_list=[1,2,3,4,5,6]
>>> #adding an element to the list
>>> my_list.append(9)
>>> #removing an element to the list
>>> my_list.remove(2)
>>> #modifying an element in the list
>>> my_list[0]=8
>>> print("update list:",my_list)
update list: [8, 3, 4, 5, 6, 9]
>>> #creating a dictionary
>>> my_dict={'name':'jeorge','age':22,'city':'delhi'}
>>> #adding an element to the dict
>>> my_dict['gender']='male'
>>> #removing an element in the dict
>>> del my_dict['age']
>>> #modifying an element in the dict
>>> my_dict['city']='goa'
>>> print("updated dictionary:",my_dict)
updated dictionary: {'name': 'jeorge', 'city': 'goa', 'gender': 'male'}
>>> #creating a set
>>> my_set={1,2,3,4,5}
>>> #adding an element to the set
>>> my_set.add(7)
>>> #removing an element from the list
>>> my_set.remove(2)
>>> #modifying an element in the list
>>> my_set.discard(1)
>>> my_set.add(9)
>>> print("updated set:",my_set)
updated set: {3, 4, 5, 7, 9}
