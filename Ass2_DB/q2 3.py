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
        CREATE TABLE meal_item(
            meal_id INT,
            item_id INT NOT NULL,
        PRIMARY KEY(meal_id, item_id),
        FOREIGN KEY(meal_id) REFERENCES menu_meal(meal_id),
        FOREIGN KEY(item_id) REFERENCES menu_item(item_id)
        );
    """)
    print(', '.join(str(row) for row in cursor.fetchall()))