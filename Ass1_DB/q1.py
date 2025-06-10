import mysql.connector 

if __name__ == '__main__': 
    mydb = mysql.connector.connect( 
        host="localhost", 
        user="root", 
        password="root", 
        database="f1_data", 
        port='3307', 
    )

    cursor = mydb.cursor() 
    cursor.execute(""" 
        SELECT DISTINCT Driver      # We dont want duplicate names
        FROM drivers
        WHERE nationality = 'BRA';  # Brazilian drivers
    """)
    print(', '.join(str(row) for row in cursor.fetchall()))