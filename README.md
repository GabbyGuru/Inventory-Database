# Inventory-Database
A  relational database designed to track user transactions, customer infomation, and purchase orders.

#Database Shcema
**tires table: 
  MariaDB [inventory_db]> describe tires;
+-------------------+---------------+------+-----+---------+-------+
| Field             | Type          | Null | Key | Default | Extra |
+-------------------+---------------+------+-----+---------+-------+
| sku               | varchar(50)   | NO   | PRI | NULL    |       |
| supplier_name     | varchar(100)  | NO   |     | NULL    |       |
| brand             | varchar(20)   | NO   |     | NULL    |       |
| width             | varchar(20)   | NO   |     | NULL    |       |
| cost              | decimal(10,2) | NO   |     | 0.00    |       |
| ratio             | int(11)       | YES  |     | NULL    |       |
| construction_type | char(1)       | NO   |     | NULL    |       |
| rim_size          | decimal(10,2) | NO   |     | NULL    |       |
| stock_quantity    | int(11)       | NO   |     | 0       |       |
+-------------------+---------------+------+-----+---------+-------+

**suppliers table:
  MariaDB [inventory_db]> describe suppliers;
+---------------+--------------+------+-----+---------+----------------+
| Field         | Type         | Null | Key | Default | Extra          |
+---------------+--------------+------+-----+---------+----------------+
| supplier_id   | int(11)      | NO   | PRI | NULL    | auto_increment |
| supplier_name | varchar(100) | NO   | UNI | NULL    |                |
| email         | varchar(100) | YES  |     | NULL    |                |
| phone         | varchar(20)  | YES  |     | NULL    |                |
+---------------+--------------+------+-----+---------+----------------+

**users table:
  MariaDB [inventory_db]> describe users;
+-----------+-------------+------+-----+---------------------+----------------+
| Field     | Type        | Null | Key | Default             | Extra          |
+-----------+-------------+------+-----+---------------------+----------------+
| user_id   | int(11)     | NO   | PRI | NULL                | auto_increment |
| username  | varchar(20) | NO   | UNI | NULL                |                |
| role      | varchar(20) | NO   |     | NULL                |                |
| create_at | timestamp   | YES  |     | current_timestamp() |                |
+-----------+-------------+------+-----+---------------------+----------------+

**inventory_transaction table:
  MariaDB [inventory_db]> describe inventory_transactions;
+------------------+--------------------------------------------------------+------+-----+---------------------+----------------+
| Field            | Type                                                   | Null | Key | Default             | Extra          |
+------------------+--------------------------------------------------------+------+-----+---------------------+----------------+
| transaction_id   | int(11)                                                | NO   | PRI | NULL                | auto_increment |
| sku              | varchar(50)                                            | NO   | MUL | NULL                |                |
| username         | varchar(50)                                            | NO   | MUL | NULL                |                |
| transaction_type | enum('Inbound/Putaway','Outbound/Picker','Adjustment') | NO   |     | NULL                |                |
| quantity         | int(11)                                                | NO   |     | NULL                |                |
| transaction_date | timestamp                                              | YES  |     | current_timestamp() |                |
| location         | varchar(20)                                            | NO   |     | NULL                |                |
+------------------+--------------------------------------------------------+------+-----+---------------------+----------------+

  **purchase_orders table:
    MariaDB [inventory_db]> describe purchase_orders;
+-------------------+-----------------------------------------------------------------------+------+-----+---------------------+-------+
| Field             | Type                                                                  | Null | Key | Default             | Extra |
+-------------------+-----------------------------------------------------------------------+------+-----+---------------------+-------+
| po_number         | varchar(15)                                                           | NO   | PRI | NULL                |       |
| sku               | varchar(50)                                                           | NO   |     | NULL                |       |
| supplier_name     | varchar(100)                                                          | NO   | MUL | NULL                |       |
| order_date        | date                                                                  | NO   |     | NULL                |       |
| expected_delivery | date                                                                  | YES  |     | NULL                |       |
| amount            | int(10)                                                               | NO   |     | NULL                |       |
| status            | enum('Pending','Ordered','Partially Received','Recieved','Cancelled') | YES  |     | NULL                |       |
| total_cost        | decimal(10,2)                                                         | YES  |     | NULL                |       |
| created_at        | timestamp                                                             | YES  |     | current_timestamp() |       |
+-------------------+-----------------------------------------------------------------------+------+-----+---------------------+-----

**po_items table:
  MariaDB [inventory_db]> describe po_items;
+-------------------+--------------+------+-----+---------------------+----------------+
| Field             | Type         | Null | Key | Default             | Extra          |
+-------------------+--------------+------+-----+---------------------+----------------+
| po_id             | int(11)      | NO   | PRI | NULL                | auto_increment |
| po_number         | varchar(15)  | NO   | MUL | NULL                |                |
| sku               | varchar(50)  | NO   | MUL | NULL                |                |
| supplier_name     | varchar(100) | NO   | MUL | NULL                |                |
| quantity_ordered  | int(11)      | YES  |     | 0                   |                |
| quantity_received | int(11)      | YES  |     | NULL                |                |
| created_at        | timestamp    | YES  |     | current_timestamp() |                |
+-------------------+--------------+------+-----+---------------------+----------------+

