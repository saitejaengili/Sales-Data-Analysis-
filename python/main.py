
from database import get_connection
from data_cleaning import clean_sales_data


def import_sales_data():

    df = clean_sales_data()

    connection = get_connection()
    cursor = connection.cursor()

    try:

        for _, row in df.iterrows():

            # 1. Insert customer
            cursor.execute("""
                INSERT INTO customers
                    (customer_name, region)
                VALUES (%s, %s)
                ON CONFLICT (customer_name)
                DO UPDATE SET region = EXCLUDED.region
                RETURNING customer_id;
            """, (
                row["customer_name"],
                row["region"]
            ))

            customer_id = cursor.fetchone()[0]

            # 2. Insert product
            cursor.execute("""
                INSERT INTO products
                    (product_name, category, unit_price, cost_price)
                VALUES (%s, %s, %s, %s)
                ON CONFLICT (product_name)
                DO UPDATE SET
                    category = EXCLUDED.category,
                    unit_price = EXCLUDED.unit_price,
                    cost_price = EXCLUDED.cost_price
                RETURNING product_id;
            """, (
                row["product_name"],
                row["category"],
                float(row["unit_price"]),
                float(row["cost_price"])
            ))

            product_id = cursor.fetchone()[0]

            # 3. Insert order
            cursor.execute("""
                INSERT INTO orders
                    (order_id, customer_id, order_date)
                VALUES (%s, %s, %s)
                ON CONFLICT (order_id)
                DO UPDATE SET
                    customer_id = EXCLUDED.customer_id,
                    order_date = EXCLUDED.order_date;
            """, (
                int(row["order_id"]),
                customer_id,
                row["order_date"].date()
            ))

            # 4. Insert sales
            cursor.execute("""
                INSERT INTO sales
                    (order_id, product_id, quantity,
                     unit_price, cost_price)
                VALUES (%s, %s, %s, %s, %s)
                ON CONFLICT (order_id, product_id)
                DO UPDATE SET
                    quantity = EXCLUDED.quantity,
                    unit_price = EXCLUDED.unit_price,
                    cost_price = EXCLUDED.cost_price;
            """, (
                int(row["order_id"]),
                product_id,
                int(row["quantity"]),
                float(row["unit_price"]),
                float(row["cost_price"])
            ))

        connection.commit()

        print("\n================================")
        print("SALES DATA IMPORT SUCCESSFUL!")
        print("================================")
        print("Records processed:", len(df))

    except Exception as error:

        connection.rollback()
        print("Data import failed:", error)
        raise

    finally:

        cursor.close()
        connection.close()


if __name__ == "__main__":
    import_sales_data()
