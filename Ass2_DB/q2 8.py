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
        CREATE TABLE full_order(
            order_id INT,
            order_time DATETIME NOT NULL,
            by_client INT NOT NULL,
        PRIMARY KEY(order_id),
        FOREIGN KEY(by_client) REFERENCES client(client_id)
        );
    """)
    print(', '.join(str(row) for row in cursor.fetchall()))