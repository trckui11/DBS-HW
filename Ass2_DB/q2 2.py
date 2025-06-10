import mysql.connector

if __name__ == '__main__':
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="burgers",
        port='3307',
    )
    cursor = mydb.cursor()
    cursor.execute("""
        CREATE TABLE menu_meal(
            meal_id INT,
            meal_name VARCHAR(200) NOT NULL,
            price SMALLINT NOT NULL,
            served_at VARCHAR(200) NOT NULL,
        PRIMARY KEY(meal_id));
    """)
    print(', '.join(str(row) for row in cursor.fetchall()))