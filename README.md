inventory_db (Inventory Database Manager)

A python base CLI application to manage a local inventory database. It handles product tracking, stock updates, and basic reporting.

## Features

* **Automation Mariadb database setup** and schema creation
* **FULL CRUD operation** (create, Read, Update, Delete) for inventory tracking
* **low stock alert triggers**

---

## Getting Starting

### prerequisites
*Kali-Linux 
*python3.x
*MYSQL / MariaDB 

---

## Installation

### 1. Install MYSQL / Mariadb

    sudo apt update 
    sudo apt install mariadb-server mariadb-client

### 2. Start the MariaDB service
    
    sudo systemctl enable mariadb

### 3. Sign into Mariadb 
    
    sudo mysql -u root -p 

 -  -u flag = Specifies the username (default is root)
-  -p flag = prompt your database root password (or kali-linux password) 

---
  
  ### Database Setup 

### 1. create a database inside mariadb 
    
    CREATE DATABASE inventory_db;

 ### 2. Switch over to the database to then create the table 

   USE inventory_db;

### 3. Create a table for the database 
    
    CREATE TABLE tires
   ( Define your attributes here )


   ### follow to schema.sql file in the repository to learn the attributes, column,data types required for the tables 


---

### Python installation 
 
### 1. create a directory for your python install. If you install it on your regular kali- linux terminal you can break your machine. So you create a directory and then a virtual environment to isolate the install and do not break anything. For this purpose we will download python in a sandbox 

        sudo mkdir inventory_project

---
### If you do not want to use sudo for the directory or it still will not install - change permissions from root to the user, update system first 
---
   
   ### 2. cd inventory_project
       
       sudo apt install python3 python3-venv python3-pip

### 3. Create the sandbox

    python -m venv venv
    
- -the second venv = the name of the sandbox
    
### 4. start the sandbox
      
      source venv/bin/activate

### 5.  Install python-dotenv to securely store database credentials and API keys without hard coding them into your script 
     
      pip install python-dotenv

### 6. To hide the file use module in the python script 

       import os
      from dotenv import_dotenv

  ### 7. Load variables from .env files 

        load_dotenv()

  ### 8. Create the python class and connect to the database 

      class InventoryAPI:
      def __init__(self):
          self.connection = None
          self.cursor = None

  ### 9. To hide the passwords in the code use these syntax

      host=os.getenv("DB_HOST")
      user=os.getenv("DB_USER")
      password=os.getenv("DB_PASSWORD")
  

      

      
