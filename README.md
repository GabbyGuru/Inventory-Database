inventory_db (Inventory Database Manager)
A python base CLI applicatioon to manage a local inventory database it handles product tracking, stcok updates, and basic resporting.

## Features
*Automation mariadb database setup and schema creation
*FULL CRUD operation (create, Read, Update, Delete) for inventory tracking
*low stock alert triggers

## Getting Starting
###prequisites
*Kali-Linux 
*python.3.x
*MYSQL / MariaDB 

### Installation 

*Install mysql / mariadb
    
    sudo apt install mariadb-server mariadb-client

Start the MariaDB service
    
    sudo systemctl enable mariadb

*Sign into maraidb 
  
  sudo mysql -u root -p 

 -u flag = Specifies the username (default is root)
 -p flag = prompt your database root password (or kali-linux password) 

  
  ## Database Setup  

  CREATE DATABASE inventory_db;

 # once the table is created- switch over to the databse to then create the table 

   USE inventory_db;

   CREATE TABLE tires
   ( Define your attributes here )


   ### follow to shcema.sql file in the repository to learn the attrubutes, column,data types required for the tables 
