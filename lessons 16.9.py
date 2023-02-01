




# numbers = input("1 2 3 4 5 6 7:")
#
# numbers_split = numbers.split()
# numbers_lines = "\n".join(numbers_split)
#
# print(numbers_lines)


# 16.9.1
# class Rectangle:
#     def __init__(self, x, y, width, height):
#         self.x = x
#         self.y = y
#         self.width = width
#         self.height = height
#
#     def __str__(self):
#         return f'Rectangle:{self.x},{self.y},{self.width},{self.height}.'
# rect_1 = Rectangle(5,10,50,100)
# print(rect_1)


# 16.9.2
# class Rectangle:
#     def __init__(self, x, y, width, height):
#         self.x = x
#         self.y = y
#         self.width = width
#         self.height = height
#
#     def __str__(self):
#         return f'Rectangle:{self.x},{self.y},{self.width},{self.height}.'
#     def get_area(self):
#         return self.width*self.height
# rect_1=Rectangle(5,10,50,100)
# print(rect_1)
# print(rect_1.get_area())


# 16.9.3
# class Clients:
#     def __init__(self, name, surname, city, balance):
#         self.name = name
#         self.surname = surname
#         self.city = city
#         self.balance = balance
#
#     def __str__(self):
#         return f'''"{self.name} {self.surname}".{self.city}.Баланс:{self.balance}руб.'''
# client_1 = Clients('Максим','Васильев','Брянск',45)
# print(client_1)


# 16.9.4
# class Clients:
#     def __init__(self, name, surname, city, balance):
#         self.name = name
#         self.surname = surname
#         self.city = city
#         self.balance = balance
#
#     def __str__(self):
#         return f'''"{self.name} {self.surname}".{self.city}.Баланс:{self.balance}руб.'''
#     def get_guest(self):
#         return f'{self.name} {self.surname},г.{self.city}'
#
# client_1 = Clients('Максим','Васильев','Брянск',45)
# client_2 = Clients('Татьяна','Петрова','Анапа', 38)
# client_3 = Clients('Ольга','Иванова','Курск', 58)
#
# guest_list=[client_1,client_2,client_3]
#
# for guest in guest_list:
#     print(guest.get_guest())



