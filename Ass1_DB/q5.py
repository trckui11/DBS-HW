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
        SELECT drivers.Car, AVG(drivers.PTS) AS avg_pts # Get the car and the avg number of points of the drivers of it
        FROM fastest_laps, drivers
        WHERE fastest_laps.Car = drivers.Car # Join the fastest_laps and drivers tables
        GROUP BY fastest_laps.Car
        # Filter out cars with fastest lap time >= 120 seconds
        HAVING MIN(TIME_TO_SEC(STR_TO_DATE(fastest_laps.Time, '%i:%s.%f'))) < 120
        ORDER BY avg_pts DESC;
    """)
    print(', '.join(str(row) for row in cursor.fetchall()))