import psycopg2
from psycopg2 import sql


db_host = "localhost"  
db_name = "your_db_name"  
db_user = "your_db_user"  
db_password = "your_db_password"  
db_port = "5432"  

try:
    
    connection = psycopg2.connect(
        host=db_host,
        database=db_name,
        user=db_user,
        password=db_password,
        port=db_port
    )

    
    cursor = connection.cursor()

   
    query = "SELECT * FROM your_table_name;"  
    cursor.execute(query)

   
    records = cursor.fetchall()

    
    print("Query results:")
    for row in records:
        print(row)

except Exception as error:
    print(f"Error connecting to PostgreSQL database: {error}")

finally:
    
    if cursor:
        cursor.close()
    if connection:
        connection.close()
