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
            SELECT 
                menu_meal.meal_name, 
                COUNT(order_item.order_id) AS meals_sold  -- count the number of meals that sold
            FROM menu_meal
            LEFT JOIN order_item -- left join the order_item table to get the meals that sold
                ON menu_meal.meal_id = order_item.item_id AND order_item.is_meal = TRUE  -- join the order_item table with the menu_meal table to get the meal_id, even if not ordered
            GROUP BY menu_meal.meal_name  -- group by the meal_name in order to get the count of meals sold
            ORDER BY meals_sold DESC;  -- order by the number of meals sold in descending order
    """)

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    mydb.close()