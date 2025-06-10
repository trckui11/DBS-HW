import mysql.connector
if __name__ == 'main':
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="burgers",
        port='3307',
    )
    cursor = mydb.cursor()
    cursor.execute("""
        UPDATE menu_meal -- update the menu_meal table
        SET raw_cost = (
            SELECT SUM(mi2.price) -- the sum of the prices of the items in the meal
            FROM meal_item AS mi 
            JOIN menu_item AS mi2 
                ON mi.item_id = mi2.item_id -- join the meal_item table with the menu_item table to get the prices of the items
            WHERE mi.meal_id = 4 -- the specific meal_id
        )
        WHERE meal_id = 4; -- small Oburger Meal (meal_id = 4)
    """)
    mydb.commit()
    cursor.close()
    mydb.close()