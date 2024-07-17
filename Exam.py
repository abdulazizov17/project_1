# Abdulazizov Asilbek A variant  

# 1-masala      

# import psycopg2
# conn = psycopg2.connect(database = 'n48',
#                         user = 'postgres',
#                         host = 'localhost',
#                         password = 'qazwsx',
#                         port = 5432
#                         )
# cursor = conn.cursor()
# create_products_table = '''create table products(
#     id serial primary key,
#     name varchar(100) not null,
#     price int,
#     color varchar(100),
#     image varchar(100)
# );
# '''
# cursor.execute(create_products_table)
# conn.commit()

# # 2-masala

# def inser_products(self):
#     insert_prodcts = '''
#     Inser into products(name,price,color,image)
#     values('Telefon',1000,'black','image')    
# '''   

# def delete_products(self):
#     delete_products_del = '''
#     DELETE from products where id = 1;
#     '''
#     cursor.execute(delete_products)
#     conn.commit()
     
# def update_prodcts(self):
#     update_table = '''
#       insert into products(name,price,color,image)
#     values(%s,%s,%s,%s);
#     '''

# 1- chi va 2- masalalarni bitta qilib ishlangani 
# import psycopg2
# conn = psycopg2.connect(database = 'n48',
#                         user = 'postgres',
#                         host = 'localhost',
#                         password = 'qazwsx',
#                         port = 5432
#                         )
# cursor = conn.cursor()

# create_products_table = '''create table products(
      
#     id serial primary key ,
#     name varchar(100),
#     price int,
#     color varchar(100) not null,
#     image varchar(100),
# );
# '''
# cursor.execute(create_products_table)
# conn.commit()

# class Products:
#     def __init__(self,name,price,color,image) -> None:
#         self.name = name,
#         self.price = price,
#         self.color = color,
#         self.image = image,
#     def save(self):
#         insert_into_query  = '''
#         inser into products(name,price,color,image)
#         values(%s,%s,%s,%s,%s,%s); 
#         ''' 
#         malumot = (self.name,self.price,self.color,self.image)
#         cursor.execute(insert_into_query)
#         conn.commit()
        
#     def delet_products(self):
#         delete_teble_del = '''
#         DELETE FROM foydalanuvchi WHERE id = 1;    
#         '''
#         cursor.execute(delete_teble_del)
#         conn.commit()
        
#     def update_products(self):
#         update_table = '''
#          inser into products(name,price,color,image)
#         values(%s,%s,%s,%s,%s,%s);
#         '''
        
            
# update_table = Products('Telefon,1000,'white','image')
# update_table.update_products

# 3-masala

# class Alphabet:
#     def __iter__(self):
#         self.current = ord('A')
#         self.end = ord('Z')
#         return self

#     def __next__(self):
#         if self.current <= self.end:
#             letter = chr(self.current)
#             self.current += 1
#             return letter
#         else:
#             raise StopIteration

# alphabet = Alphabet()
# for letter in alphabet:
#     print(letter, end=' ')
        
        
# 4-masala


# import threading
# import time

# def print_numbers():
#     for i in range(1, 6):
#         print(i)
#         time.sleep(1)

# def print_letters():
#     for letter in 'ABCDE':
#         print(letter)
#         time.sleep(1)

# thread1 = threading.Thread(target=print_numbers)
# thread2 = threading.Thread(target=print_letters)
# thread1.start()
# thread2.start()
# thread1.join()
# thread2.join()


# 5-masala


# import psycopg2
# conn = psycopg2.connect(database = 'n48',
#                         user = 'postgres',
#                         host = 'localhost',
#                         password = 'qazwsx',
#                         port = 5432
#                         )
# cursor = conn.cursor()

# create_users_table = '''create table users(
      
#     id serial primary key ,
#     first_name varchar(100),
#     username varchar(100),
#     email varchar(100) not null,
#     age int,
#     is_active bool
# );
# '''
# cursor.execute(create_users_table)
# conn.commit()

# class User:
#     def __init__(self,first_name,last_name,username,email,age,is_active) -> None:
#         self.first_name = first_name,
#         self.last_name = last_name,
#         self.username = username,
#         self.email = email,
#         self.age = age,
#         self.is_active = is_active
#     def save(self):
#         insert_into_query  = '''
#         inser into users(firs_name,last_name,username,email,age,is_active)
#         values(%s,%s,%s,%s,%s,%s); 
#         ''' 
#         malumot = (self.firs_name,self.last_name,self.username,self.email,self.age,self.is_active)
#         cursor.execute(insert_into_query)
#         conn.commit()
                
#     def update_user(self):
#         update_table = '''
#          inser into users(firs_name,last_name,username,email,age,is_active)
#         values(%s,%s,%s,%s,%s,%s);
#         '''
            
# update_table = User('John','Doe','johndoe','johndoe37@gmail.com',32,True)
# update_table.update_user     
# user_male = User('Jek','William','Jekkk','jek@gmail.com',38,True)
# user_male.save
# user_female = User('Anna','Jolie','annijolie','anna90@gmail.com',18,True)
# user_female.save

# # 6- masala

# import psycopg2
# db_conn = {
#     'database': 'n48',
#     'user': 'postgres',
#     'password': 'qazwsx',
#     'host': 'localhost',
#     'port': 5432
# }
# class DatabaseConnect:
#     def __init__(self, db_conn) -> None:
#         self.db_conn = db_conn
    
#     def __enter__(self):
#         self.conn = psycopg2.connect(**self.db_conn)
#         self.cur = self.conn.cursor()
#         return self.cur
    
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if exc_type or exc_val or exc_tb:
#             self.conn.rollback()
#         else:
#             self.conn.commit()
#         self.cur.close()
#         self.conn.close()
# class DbConnect:
#     def __init__(self,db_conn) -> None:
#         self.db_conn = db_conn
#         with DatabaseConnect(self.db_conn) as cursor:
#             cursor.execute('''
#                 create table if not exists exam(
#                     id serial primary key,
#                     savol varchar(100),
#                     javob varchar(100)
#                 )
#             ''')
#     def create_exam(self,savol,javob):
#         with DatabaseConnect(self.db_conn) as cursor:
#             cursor.execute('''
#                 insert into exam(savol,javob)
#                 values(%s,%s)
#                 ''',(savol,javob))
# exam_manager = DbConnect(db_conn)
# exam_manager.create_exam('6.	DbConnect nomli ContextManager yarating. Va uning vazifasi python orqali PostGresqlga ulanish (conn,cur)',
#                          '6-masaladagi kodda yozilgan javobi')



#7-masala


import psycopg2
import json
import requests

conn = psycopg2.connect(
    dbname="n48", 
    user="postgres", 
    password="qazwsx", 
    host="localhost", 
    port=5432
)
cur = conn.cursor()
create_table_query = '''
    CREATE TABLE IF NOT EXISTS products (
        id SERIAL PRIMARY KEY,
        title VARCHAR(255),
        description TEXT,
        price DECIMAL,
        discountPercentage DECIMAL,
        rating DECIMAL,
        stock INT,
    );
'''
cur.execute(create_table_query)
conn.commit()  

url = "https://dummyjson.com/products"
response = requests.get(url)
products = response.json()['products']
for product in products:
    print(product)  
    cur.execute("""
        INSERT INTO products(title, description, price, discountPercentage, rating, stock)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (
        product['title'],
        product['description'],
        product['price'],
        product['discountPercentage'],
        product['rating'],
        product['stock'], 
    ))
conn.commit()
cur.close()
conn.close()









