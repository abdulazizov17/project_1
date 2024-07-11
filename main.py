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
    CREATE TABLE IF NOT EXISTS productus (
        id SERIAL PRIMARY KEY,
        title VARCHAR(255),
        description TEXT,
        price DECIMAL,
        discountPercentage DECIMAL,
        rating DECIMAL,
        stock INT,
        brand VARCHAR(255),
        category VARCHAR(255),
        thumbnail VARCHAR(255),
        weight DECIMAL
    );
'''
cur.execute(create_table_query)
conn.commit()  

url = "https://dummyjson.com/products"
response = requests.get(url)
productus = response.json()['products']
for product in productus:
    print(product)  
    cur.execute("""
        INSERT INTO productus (title, description, price, discountPercentage, rating, stock, brand, category, thumbnail, weight)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        product['title'],
        product['description'],
        product['price'],
        product['discountPercentage'],
        product['rating'],
        product['stock'],
        product['brand'],
        product['category'],
        product['thumbnail'],
        product.get('weight', None)  
    ))
conn.commit()
cur.close()
conn.close()
