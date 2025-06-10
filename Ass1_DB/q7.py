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
        # List all unique drivers who either:
        # won a race with Ferrari, OR
        # are from France
        SELECT DISTINCT drivers.Driver
        FROM winners, drivers
        # Join the winners and drivers tables
        # on the condition that the driver won  
        WHERE (drivers.Driver = winners.Winner AND 
            winners.Car = 'Ferrari') 
        # OR the driver is from France
        OR drivers.Nationality = 'FRA'
        # Order the results by driver name
        ORDER BY drivers.Driver;
    """)
    print(', '.join(str(row) for row in cursor.fetchall()))