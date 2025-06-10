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
        SELECT mm.meal_name -- we want to select only the meal name
            FROM menu_meal AS mm
            JOIN meal_item AS mi
                ON mm.meal_id = mi.meal_id -- join the menu_meal table with the meal_item table to get the meal_id
            JOIN menu_item AS it
                ON mi.item_id = it.item_id
            GROUP BY
            mm.meal_id,
            mm.meal_name,
            mm.price -- group by the meal_id, meal_name and price in order to get the sum of the prices of the items in the meal
            HAVING mm.price >= SUM(it.price); -- we want to select only the meals that have a price greater than or equal to the sum of the prices of the items in the meal

    """)
    print(', '.join(str(row) for row in cursor.fetchall()))