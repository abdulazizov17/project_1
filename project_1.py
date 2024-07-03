import psycopg2
conn = psycopg2.connect(database = 'n48',
                        user = 'postgres',
                        host = 'localhost',
                        password = 'qazwsx',
                        port = 5432
                        )
cursor = conn.cursor()

create_foydalanuvchi_table = '''create table foydalanuvchi(
      
    id serial primary key ,
    first_name varchar(100),
    username varchar(100),
    email varchar(100) not null,
    age int,
    is_active bool
);
'''
cursor.execute(create_foydalanuvchi_table)
conn.commit()

class User:
    def __init__(self,first_name,last_name,username,email,age,is_active) -> None:
        self.first_name = first_name,
        self.last_name = last_name,
        self.username = username,
        self.email = email,
        self.age = age,
        self.is_active = is_active
    def save(self):
        insert_into_query  = '''
        inser into foydalanuvchi(firs_name,last_name,username,email,age,is_active)
        values(%s,%s,%s,%s,%s,%s); 
        ''' 
        malumot = (self.firs_name,self.last_name,self.username,self.email,self.age,self.is_active)
        cursor.execute(insert_into_query)
        conn.commit()
        
    def delet_user(self):
        delete_teble_del = '''
        DELETE FROM foydalanuvchi WHERE id = 1;    
        '''
        cursor.execute(delete_teble_del)
        conn.commit()
        
    def update_user(self):
        update_table = '''
         inser into foydalanuvchi(firs_name,last_name,username,email,age,is_active)
        values(%s,%s,%s,%s,%s,%s);
        '''
        
            
update_table = User('Kevin','Bruno','Kevindebrune','kevindebruno17@gmail.com',32,True)
update_table.update_user     
user_male = User('john','Doe','johnDoe','joh@gmail.com',32,True)
user_male.save
user_female = User('Anna','Asti','anniasti','anna10@gmail.com',27,True)
user_female.save
