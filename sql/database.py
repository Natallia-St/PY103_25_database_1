import sqlite3
import random

# TASK1########################################
# conn = sqlite3.connect('name.database')
# cursor = conn.cursor()
# cursor.execute(
#     '''CREATE TABLE IF NOT EXISTS
#         tab_3(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name_item TEXT,
#         who_write TEXT,
#         cost INTEGER
#     )
#      ''')
# name = "Поиск"
# writer = "Петров"
# price = int(input("Введите стоимость"))
# cursor.execute("""
# INSERT INTO
#     tab_3(name_item, who_write, cost )
# VALUES(?,?,?)
# """, (name, writer, price))
# conn.commit()
#
# for i in cursor.execute('''SELECT*FROM tab_3'''):
#     e=0
#     h=list(i)
#     m=" ".join(str(e) for e in h)
#     print(e)
#


# # # TASK2##########################################
# conn = sqlite3.connect('name.database_2')
# cursor = conn.cursor()
# cursor.execute(
#     '''CREATE TABLE IF NOT EXISTS
#         tab_8(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         num_1 INTEGER,
#         num_2 INTEGER
#
#     )
#     ''')
# data_list = [(random.randint(10,15), random.randint(10,15) )  for i in range(0,10)]
# print(data_list)
#
# # for _tuple in data_list:
# #     cursor.execute("""
# #     INSERT INTO
# #         tab_8(num_1, num_2 )
# #     VALUES(?,?)
# #     """, (_tuple))
# # conn.commit()
# cursor.execute('''SELECT * FROM tab_8''')
# print("без удаления", cursor.fetchall())
#
#
# sum1=0
# # sum2=0
# count1=0
# # count2=0
# for i in cursor.execute("""SELECT num_1, num_2 FROM tab_8"""):
#     for j in i:
#         sum1+=j
#         count1+=1
# print(sum1, count1)
# cursor.execute('''SELECT * FROM tab_8''')
# count_of_tuple=len(cursor.fetchall())
# if sum1/count1>count_of_tuple:
#     cursor.execute("""DELETE  FROM tab_8 WHERE ID=4""")
#
# cursor.execute('''SELECT * FROM tab_8''')
# print("с удалением", cursor.fetchall())

# #TASK3#########################################
# conn = sqlite3.connect('name.database_3')
# cursor = conn.cursor()
# cursor.execute(
#     '''CREATE TABLE IF NOT EXISTS
#         tab_9(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         num_1 INTEGER,
#         num_2 INTEGER
#
#     )
#     ''')
# data_list = [(random.randint(0,9), random.randint(0,9) )  for i in range(0,10)]
# # print(data_list)
#
# # for _tuple in data_list:
# #     cursor.execute("""
# #     INSERT INTO
# #         tab_9(num_1, num_2 )
# #     VALUES(?,?)
# #     """, (_tuple))
# # conn.commit()
# cursor.execute('''SELECT * FROM tab_9''')
# print("без корре", cursor.fetchall())
#
# cursor.execute('''SELECT ID FROM tab_9''')
# data_id= cursor.fetchall()
# id_random = random.choice(data_id)
# print(id_random)
# cursor.execute('''SELECT num_1, num_2 FROM tab_9 WHERE ID=?''', (id_random))
# tuple_=cursor.fetchall()
#
# n=0 #четное
# m=0
# for i in tuple_:
#     for j in i:
#         if j%2==0:
#             n+=1
#         else:
#             m+=1
# if n==2:
#     cursor.execute('''DELETE  FROM tab_9 WHERE ID=?''', (id_random))
#     cursor.fetchall()
#     conn.commit()
# elif m==2:
#     cursor.execute('''UPDATE tab_9 SET num_1=2, num_2=2 WHERE ID=?''', (id_random))
#     cursor.fetchall()
#     conn.commit()
# print("n", n, "m", m, )
# cursor.execute('''SELECT * FROM tab_9''')
# print(cursor.fetchall())



# #TASK4#########################################
# conn = sqlite3.connect('name.database_4')
# cursor = conn.cursor()
# cursor.execute(
#     '''CREATE TABLE IF NOT EXISTS
#         tab_9(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         num INTEGER
#
#     )
#     ''')
#
# class Base_special:
#     def __init__(self, var1=None, var2=None, var3=None):
#         self.var1=var1
#         self.var2=var2
#         self.var3=var3
#     def change_database(self):
#         if self.var1 is not None and self.var2 is None and self.var3 is None:
#             cursor.execute('''INSERT INTO tab_9 (num) VALUES(?)''', (3,))
#             conn.commit()
#         elif self.var1 is not None and self.var2 is not None and self.var3 is None:
#             if type(self.var2)==int:
#                 cursor.execute('''DELETE FROM tab_9 WHERE ID =?''', (1,))
#                 conn.commit()
#         elif self.var1 is not None and self.var2 is not None and self.var3 is not None:
#             if type(self.var3)==int:
#                 cursor.execute("""UPDATE tab_9 SET num=77 WHERE ID=3""")
#                 conn.commit()
#
#
# object=Base_special(111, "ssasa", 7)
# object.change_database()
# cursor.execute("""SELECT * FROM tab_9""")
# print(cursor.fetchall())
#
# #TASK5#########################################
# import csv
# file_data=open("file_data.csv", "w", encoding="UTF-8")
# f=open('bd.txt', "w")
# writer_=csv.writer(file_data, delimiter = ",")
#
# conn = sqlite3.connect('name.database_5')
# cursor = conn.cursor()
# cursor.execute(
#     '''CREATE TABLE IF NOT EXISTS
#         tab_10(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         num_1 TEXT,
#         num_2 TEXT

    # )
    # ''')
# n=0
# while n<3:
#     data_1=input("Введите данные для num_1")
#     data_2 = input("Введите данные для num_2")
#     cursor.execute('''INSERT INTO tab_10(num_1, num_2) VALUES (?,?) ''', (data_1, data_2))
#     conn.commit()
#     n+=1
# cursor.execute('''DELETE FROM tab_10 WHERE ID=2''')
# conn.commit()
# cursor.execute("""UPDATE tab_10 SET num_1 = 'hello', num_2= 'world' WHERE ID = 3""")
# conn.commit()
# cursor.execute("""SELECT * FROM tab_10""")
# info=(cursor.fetchall())
#
# p=[]
# for i in info:
#     i=list(i)
#     p.append(i)
# print(p)
# for i in p:
#     for j in i:
#         j= str(j)
#         f.write(j + " ")
#     f.write('\n')
# f.close()
# r=open('bd.txt')
# s=r.readlines()
# print(s)
#
# for i in info:
#     writer_.writerow(i)
# file_data.close()
#

# #TASK6###############################################
conn_1 = sqlite3.connect("my_base_1") # Создание БД
cursor_1 = conn_1.cursor() # Создаем объект курсор для работы с БД
cursor_1.execute("""CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, text_1 TEXT)""") # Заполняем БД
conn_1.commit() # Сохраняем БД

conn_2=sqlite3.connect("my_base_2") # Создание БД
cursor_2=conn_2.cursor() # Создаем объект курсор для работы с БД
cursor_2.execute("""CREATE TABLE IF NOT EXISTS tab_1 (id INTEGER PRIMARY KEY AUTOINCREMENT, num_1 INTEGER)""")
conn_2.commit() # Сохранение БД


# cursor_1.execute(""" DELETE FROM tab_1""") # Удаляем все записи из таблицы
# cursor_2.execute(""" DELETE FROM tab_1""") # Удаляем все записи из таблицы

list_=[1, "ночь", "black", 8, 10] # Список с данными для внесения в БД
for i in list_:
    if type(i)==str:
        cursor_1.execute('''INSERT INTO tab_1(text_1) VALUES (?) ''', (i,)) # с
        conn_1.commit() # Заполнение БД
        len_=len(i) # Подсчет к-ва записей в БД
        cursor_2.execute('''INSERT INTO tab_1(num_1) VALUES (?)''', (len_,)) # # Заполнение БД
        conn_2.commit()
    if type(i)==int:
        if i%2==0:
            cursor_2.execute('''INSERT INTO tab_1(num_1) VALUES(?)''', (i,)) # Заполнение БД
            conn_2.commit() # Сохранение БД
        else:
            cursor_1.execute('''INSERT INTO tab_1(text_1) VALUES(?)''', ('нечетное',)) # Заполнение БД
            conn_1.commit() # Сохранение БД

cursor_1.execute("""SELECT * FROM tab_1""") # Выборка всех данных из БД
info_in_base_1 = cursor_1.fetchall() # Получение отобранных данных
print("таблица text до изменений", info_in_base_1) # Печать данных в виде списка кортежа

cursor_2.execute("""SELECT * FROM tab_1""") # Выборка всех данных из БД
info_in_base_2 = cursor_2.fetchall() # Получение отобранных данных
print("таблица int до изменений", info_in_base_2) # Печать данных в виде списка кортежа


if len(info_in_base_2) >5:
    cursor_1.execute('''DELETE FROM tab_1 WHERE ID=108''') # Удаление записи из БД по айди
    conn_1.commit() # Сохранение БД
else:
    cursor_1.execute('''UPDATE tab_1 SET text_1="HELLOW" WHERE ID=108''') # Обновление БД для конкретного айди
    conn_1.commit() # Сохранение БД

cursor_1.execute('''SELECT * FROM tab_1 ''') # Выборка всех данных из БД
print(cursor_1.fetchall()) # Печать данных в виде списка кортежа
cursor_2.execute('''SELECT * FROM tab_1''') # Печать данных в виде списка кортежа
print(cursor_2.fetchall())




