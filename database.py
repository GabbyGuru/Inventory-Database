import os

import mysql.connector
from dotenv import load_dotenv

load_dotenv()


class InventoryAPI:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=os.getenv("DB_HOST"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
                database=os.getenv("DB_NAME"),
            )
            # dictionary=true returns rows as python dictionaries for easier reading
            self.cursor = self.connection.cursor(dictionary=True)
            print(f"Successfully connected to {os.getenv('DB_NAME')}")
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def cleantext(self, text, size=244):
        # sanitize incoming text inputs
        if not text:
            return ""
        text = text.strip()
        text = text[:size]
        if self.connection:
            text = self.connection.converter.escape(text)
        return text

    # — 1. AUDIT TRAIL (users + inventory_transactions + tires)—-

    def get_transactions_history(self, limit=10):
        """
        tracks which user moved inventory. Joins 3 tables: inventory_transactions, users, and tires.
        """
        query = """
            SELECT
                it.transaction_id,
                it.transaction_type,
                it.quantity,
                it.transaction_date,
                t.brand,
                t.sku,
                u.username
            FROM inventory_transactions it
            JOIN tires t on it.sku = t.sku
            JOIN users u on it.username = u.username
            ORDER BY it.transaction_date desc
            LIMIT %s
            """

        try:
            # ensure limit is a strict integer
            self.cursor.execute(query, (int(limit),))
            return self.cursor.fetchall()
        except mysql.connector.Error as err:
            print(f"Query Failed: {err}")
            return []

    # -- 2. LOW STOCK ALERT (tires + inventory_transactions)

    def get_low_stock_alert(self, threshold=20):
        """
        finds current stock below threshold
        """
        query = """
            SELECT
            t.brand,
            it.sku,
            SUM(it.quantity) as current_stock
            FROM inventory_transactions it
            JOIN tires t on it.sku = t.sku
            GROUP BY it.sku
            HAVING sum(it.quantity) < %s
        """

        try:
            self.cursor.execute(query, (threshold,))
            return self.cursor.fetchall()
        except mysql.connector.Error as err:
            print(f"Error fetching low_stock_alert: {err}")
            return []


# --Test 1: history test
if __name__ == "__main__":
    api = InventoryAPI()
    api.connect()
    print("\nFetching latest inventory transactions . . .")
    history = api.get_transactions_history(limit=5)

    for row in history:
        print(row)

# -- Test 2: Low Stock Check
if __name__ == "__main__":
    api = InventoryAPI()
    api.connect()
    print("Running low stock check")
    low_stock_items = api.get_low_stock_alert(20)

    if not low_stock_items:
        print("All Items are fully stocked")
    else:
        for item in low_stock_items:
            print(
                f"ALERT: {item['brand']} (SKU: {item['sku']}) is running low! Current Stock: {item['current_stock']}"
            )
