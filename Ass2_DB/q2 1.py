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
        CREATE TABLE menu_item(
            item_id INT,
            item_name VARCHAR(200) NOT NULL,
            price SMALLINT NOT NULL,
        PRIMARY KEY(item_id));
    """)
    print(', '.join(str(row) for row in cursor.fetchall()))