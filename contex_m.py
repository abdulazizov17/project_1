# import psycopg2
# db_conn = {
#     'database': 'n48',
#     'user': 'postgres',
#     'password': 'qazwsx',
#     'host': 'localhost',
#     'port': 5432
# }

# class DatabaseConnect:
#     def __init__(self,db_conn) -> None:
#         self.db_conn = db_conn
    
#     def __enter__(self):
#         self.conn = psycopg2.connect(**db_conn)
        
#         self.cur = self.conn.cursor()
#         return self.conn,self.cur
    
#     def __exit__(self,exc_type,exc_val,exc_tb):
#         if self.conn:
#             self.conn.close()
            
#         if self.cur:
#             self.cur.close()
#             self.conn.close()
# class Book:
#     def __init__(self, db_conn='books.db'):
#         self.db_conn = db_conn
#         with DatabaseConnect(self.db_conn) as cursor:
#             cursor.execute()
#             ('''
#                 CREATE TABLE IF NOT EXISTS books (
#                     id INT PRIMARY KEY,
#                     title TEXT,
#                     author TEXT,
#                     year INT
#                 )
#             ''')
#             cursor.commit()
            
#     def create_book(self,title,author,year):
#          with DatabaseConnect(self.db_conn) as cursor:
#             cursor.execute('''
#                 INSERT INTO books (title, author, year) VALUES (?, ?, ?)
#             ''', (title, author, year))
    
#     def read_books(self):
#         with DatabaseConnect(self.db_conn) as cursor:
#             cursor.execute('SELECT * FROM books')
#             return cursor.fetchall()
    
#     def update_book(self, book_id, title, author, year):
#         with DatabaseConnect(self.db_conn) as cursor:
#             cursor.execute('''
#                 UPDATE books
#                 SET title = ?, author = ?, year = ?
#                 WHERE id = ?
#             ''', (title, author, year, book_id))
    
#     def delete_book(self, book_id):
#         with DatabaseConnect(self.db_conn) as cursor:
#             cursor.execute('DELETE FROM books WHERE id = ?', (book_id,))
# book_manager = Book()
# book_manager.create_book('Python Programming', 'John Doe', 2020)
# books = book_manager.read_books()
# print(books)

# book_manager.update_book(1, 'Advanced Python Programming', 'John Doe', 2021)

# books = book_manager.read_books()
# print(books)
# book_manager.delete_book(1)
# books = book_manager.read_books()
# print(books)


#---------------------------------------------------------------------------------------------------

import psycopg2

db_conn = {
    'database': 'n48',
    'user': 'postgres',
    'password': 'qazwsx',
    'host': 'localhost',
    'port': 5432
}

class DatabaseConnect:
    def __init__(self, db_conn) -> None:
        self.db_conn = db_conn
    
    def __enter__(self):
        self.conn = psycopg2.connect(**self.db_conn)
        self.cur = self.conn.cursor()
        return self.cur
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type or exc_val or exc_tb:
            self.conn.rollback()
        else:
            self.conn.commit()
        self.cur.close()
        self.conn.close()

class Book:
    def __init__(self, db_conn):
        self.db_conn = db_conn
        with DatabaseConnect(self.db_conn) as cursor:
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS books (
                    id SERIAL PRIMARY KEY,
                    title TEXT,
                    author TEXT,
                    year INT
                )
            ''')

    def create_book(self, title, author, year):
        with DatabaseConnect(self.db_conn) as cursor:
            cursor.execute('''
                INSERT INTO books (title, author, year) VALUES (%s, %s, %s)
            ''', (title, author, year))

    def read_books(self):
        with DatabaseConnect(self.db_conn) as cursor:
            cursor.execute('SELECT * FROM books')
            return cursor.fetchall()

    def update_book(self, book_id, title, author, year):
        with DatabaseConnect(self.db_conn) as cursor:
            cursor.execute('''
                UPDATE books
                SET title = %s, author = %s, year = %s
                WHERE id = %s
            ''', (title, author, year, book_id))

    def delete_book(self, book_id):
        with DatabaseConnect(self.db_conn) as cursor:
            cursor.execute('DELETE FROM books WHERE id = %s', (book_id,))
book_manager = Book(db_conn)
book_manager.create_book('Python Programming', 'John Doe', 2020)
books = book_manager.read_books()
print(books)

book_manager.update_book(1, 'Advanced Python Programming', 'John Doe', 2021)
books = book_manager.read_books()
print(books)

book_manager.delete_book(1)
books = book_manager.read_books()
print(books)

            