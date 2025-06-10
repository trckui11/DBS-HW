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
        SELECT 
            Nationality, (
                SELECT AVG(da.PTS) FROM drivers AS da       # Avg points of drivers with the same nationality group
                WHERE da.Nationality = d.Nationality 
            ) AS avg_pts, (
                SELECT MIN(Time) FROM fastest_laps          # Min lap time of drivers in the nationality group
                WHERE fastest_laps.driver in (
                    SELECT df.driver FROM drivers AS df
                    WHERE df.Nationality = d.Nationality
                )
            ) AS min_time, (
                SELECT MAX(Date) FROM winners               # Latest date of wins of drivers in the nationality group
                WHERE winner in (
                    SELECT dw.driver FROM drivers AS dw 
                    WHERE dw.Nationality = d.Nationality
                )
            ) AS latest
        FROM drivers AS d
        GROUP BY d.Nationality;                             # Make general groups of nationalities
    """)
    print(', '.join(str(row) for row in cursor.fetchall()))