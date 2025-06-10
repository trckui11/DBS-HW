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
        SELECT pm.net_orders
            FROM (
                -- compute net_orders for each meal
                SELECT -- I want to select the amount of orders that bought the meal directly
                    mm.meal_name,
                    (
                    SELECT COUNT(*) -- for the amount
                    FROM order_item oi
                    WHERE oi.is_meal = TRUE -- I want to count this id if it is a meal
                        AND oi.item_id = mm.meal_id 
                    )
                    -
                    (
                    -- orders that bought every ingredient separately
                    SELECT COUNT(*) -- for the amount
                    FROM (
                        SELECT oi2.order_id
                        FROM order_item oi2
                        JOIN meal_item mi
                        ON oi2.item_id = mi.item_id -- join the order_item table with the meal_item table to get the meal_id
                        AND mi.meal_id = mm.meal_id -- we will take just the ing' of the specific meal_id
                        WHERE oi2.is_meal = FALSE -- now I want to count this id if it is not a meal
                        GROUP BY oi2.order_id 
                        HAVING COUNT(*) = ( -- I want to make sure that the order has all the ingredients of the meal (count for each ingredient)
                        SELECT COUNT(*)
                        FROM meal_item
                        WHERE meal_id = mm.meal_id -- this specific meal_id that we are looking for (inner query)
                        )
                    ) AS complete_orders
                    ) AS net_orders
                FROM menu_meal AS mm
            ) AS pm
            WHERE pm.net_orders = (
                -- find the smallest net_orders across all meals
                SELECT MIN(net_orders) -- get the minimum net_orders value among all meals
                FROM (
                    SELECT
                    (
                        SELECT COUNT(*) -- count direct meal orders again
                        FROM order_item oi
                        WHERE oi.is_meal = TRUE -- only count rows marked as meals
                        AND oi.item_id = mm2.meal_id -- matching this second-pass meal_id
                    )
                    -
                    (
                        -- count orders that include every ingredient separately again
                        SELECT COUNT(*) -- count how many orders qualify
                        FROM (
                            SELECT oi3.order_id
                            FROM order_item oi3
                            JOIN meal_item mi3
                                ON oi3.item_id = mi3.item_id -- link each order_item to its meal_item
                            AND mi3.meal_id = mm2.meal_id -- for this specific meal in the second pass
                            WHERE oi3.is_meal = FALSE -- consider only non-meal items
                            GROUP BY oi3.order_id 
                            HAVING COUNT(*) = ( -- ensure the order has exactly all ingredients for the meal
                                SELECT COUNT(*) 
                                FROM meal_item
                                WHERE meal_id = mm2.meal_id -- count of ingredients for this meal (inner-inner query)
                            )
                        ) AS complete_orders2
                    )
                    AS net_orders -- subtract complete-ingredient orders from direct meal orders
                    FROM menu_meal AS mm2 -- iterate this logic over all meals a second time
                ) AS all_nets
            );




    """)
    print(', '.join(str(row) for row in cursor.fetchall()))