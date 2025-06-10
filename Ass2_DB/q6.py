import mysql.connector
if __name__ == 'main':
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="burgers",
        port='3307',
    )
    cursor = mydb.cursor()
    cursor.execute("""
        ALTER TABLE menu_meal ADD raw_cost INT; 
    """)
    mydb.commit()
    cursor.close()
    mydb.close()