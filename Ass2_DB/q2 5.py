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
        CREATE TABLE street(
            street_id INT,
            street_name VARCHAR(200) NOT NULL,
            in_city INT NOT NULL,
        PRIMARY KEY(street_id),
        FOREIGN KEY(in_city) REFERENCES city(city_id)
        );
    """)
    print(', '.join(str(row) for row in cursor.fetchall()))