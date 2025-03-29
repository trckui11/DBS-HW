import mysql.connector

if __name__ == '__main__':
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="covid_db",
        port='3307',
    )
    cursor = mydb.cursor()
    cursor.execute("""
        SELECT date, new_cases
        FROM covid_db.covid_deaths
        WHERE location = 'Israel'
        ORDER BY new_cases DESC
        LIMIT 20;
    """)
    print(', '.join(str(row) for row in cursor.fetchall()))