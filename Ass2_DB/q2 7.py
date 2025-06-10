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
        CREATE TABLE client(
            client_id INT,
            client_name VARCHAR(200) NOT NULL,
            client_address INT NOT NULL,
        PRIMARY KEY(client_id),
        FOREIGN KEY(client_address) REFERENCES address(address_id)
        );
    """)
    print(', '.join(str(row) for row in cursor.fetchall()))