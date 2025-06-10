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
            # Find the driver who won at least once in 2000
            # and had the highest total laps completed.
            # Return that driver's name and their best lap time.
            SELECT Winner, MIN(f1.Time) AS min_time
            FROM winners AS w1, fastest_laps AS f1
            WHERE w1.Winner = f1.Driver
            AND EXISTS (
                SELECT *
                FROM winners AS w
                WHERE YEAR(w.Date) = 2000
                AND w1.Winner = w.Winner
            )
            GROUP BY Winner
            HAVING SUM(Laps) >= ALL (
                # Compare with total laps of all drivers who won in 2000
                SELECT SUM(Laps)
                FROM winners AS w2, fastest_laps AS f2
                WHERE w2.Winner = f2.Driver
                AND EXISTS (
                    SELECT *
                    FROM winners AS w3
                    WHERE YEAR(w3.Date) = 2000
                    AND w2.Winner = w3.Winner
                )
                GROUP BY w2.Winner
            );
    """)
    print(', '.join(str(row) for row in cursor.fetchall()))