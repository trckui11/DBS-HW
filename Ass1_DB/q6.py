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
        SELECT    w1.`Grand Prix` AS GP1, w2.`Grand Prix` AS GP2, w1.Laps   # Two Grand Prixs and laps
        FROM      winners AS w1, winners AS w2                              # Aliased 2 winners tables
        WHERE     w1.Laps >= 120                                            # More than 120 laps
        AND       w1.Laps = w2.Laps                                         # Same number of laps
        AND       w1.`Grand Prix` < w2.`Grand Prix`;                        # Alphabetically ordered and different
    """)
    print(', '.join(str(row) for row in cursor.fetchall()))