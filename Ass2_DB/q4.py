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
            city.city_name,
            COUNT(CASE WHEN menu_meal.served_at = 'morning' THEN 1 END) AS breakfasts, # we put 1 when the meal is a breakfast
            COUNT(CASE WHEN menu_meal.served_at = 'all day' THEN 1 END) AS regular_meals # we put 1 when the meal is a regular meal
        # Join all the tables to get the meals and the cities of the people who ordered them in one row:
        # menu_meal is in an order_item which is in a full_order which was made by a
        # client who has an address which has a street which is in a city
        FROM city
        JOIN street ON street.in_city = city.city_id
        JOIN address ON address.in_street = street.street_id
        JOIN client ON client.client_address = address.address_id
        JOIN full_order ON full_order.by_client = client.client_id
        JOIN order_item ON order_item.order_id = full_order.order_id
        JOIN menu_meal ON order_item.item_id = menu_meal.meal_id
        WHERE order_item.is_meal = 1 # We only want the meals, not the items
        GROUP BY city.city_name # We group by city name to be able to count things per city
        ORDER BY city.city_name; # Order alphabetically by city name
    """)
    print(', '.join(str(row) for row in cursor.fetchall()))