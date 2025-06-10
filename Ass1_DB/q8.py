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
        SELECT ABS((                                                # Difference = |a - b|
                SELECT SUM(PTS) FROM teams WHERE Team = 'Ferrari'   # Total points of Ferrari
            ) - (
                SELECT SUM(PTS) FROM teams WHERE Team = 'Maserati'  # Total points of Maserati
            )) AS diff;                                             # Label the difference as diff
    """)
    print(', '.join(str(row) for row in cursor.fetchall()))