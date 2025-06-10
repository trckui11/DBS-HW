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
            # Count how many races were won in 2001 by the cars
            # that won the most races in 1999
            SELECT COUNT(*)
            FROM winners AS w3
            WHERE Car IN (
                # Find the cars with the most wins in 1999
                SELECT Car
                FROM (
                    SELECT Car, COUNT(*) AS num_of_winnings
                    FROM winners AS w
                    WHERE YEAR(w.Date) = 1999
                    GROUP BY Car
                ) AS car_wins
                WHERE num_of_winnings >= ALL (
                    # Get the highest number of wins by any car in 1999
                    SELECT COUNT(*) AS num_of_winnings
                    FROM winners AS w2
                    WHERE YEAR(w2.Date) = 1999
                    GROUP BY Car
                )
            ) AND YEAR(w3.Date) = 2001;
    """)
    print(', '.join(str(row) for row in cursor.fetchall()))