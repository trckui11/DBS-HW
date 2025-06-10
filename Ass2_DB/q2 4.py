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
        CREATE TABLE city(
            city_id INT,
            city_name VARCHAR(200) NOT NULL,
        PRIMARY KEY(city_id)
        );
    """)
    print(', '.join(str(row) for row in cursor.fetchall()))