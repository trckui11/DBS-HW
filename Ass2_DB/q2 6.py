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
        CREATE TABLE address(
            address_id INT,
            in_street INT NOT NULL,
            street_number SMALLINT NOT NULL,
            floor SMALLINT NOT NULL,
        PRIMARY KEY(address_id),
        FOREIGN KEY(in_street) REFERENCES street(street_id)
        );
    """)
    print(', '.join(str(row) for row in cursor.fetchall()))