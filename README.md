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

### Installation (bash)

*Install mysql / mariadb
    
    sudo apt install mariadb-server mariadb-client

Start the MariaDB service
    
    sudo systemctl enable mariadb

Sign into maraidb 
    
    sudo mysql -u root -p 

 -u flag = Specifies the username (default is root)
 -p flag = prompt your database root password (or kali-linux password) 

  
  ## Database Setup  

  CREATE DATABASE inventory_db;

 # Switch over to the database to then create the table 

   USE inventory_db;

   CREATE TABLE tires
   ( Define your attributes here )


   ### follow to shcema.sql file in the repository to learn the attrubutes, column,data types required for the tables 

## python installation 
 
* create a directory for your pythin install. if you install it on your regular kali- linux termal you can break yoour machone. So you create a directory and then a virtual envinment to isolate the install and dont break anything. for this purpose we will download oython in a sandbox 

        sudo mkdir inventory_project

# if you do not want to use sudo for the directory or it sill will not install - change permissions from root to the user 
# update system first 
   
   *cd inventtory_project
       
       sudo apt install python3 python3-venv python3 pip

   * create the sandbox

    python -m venv venv
     - the second venv = the name of the sandbox
    
    * start the sandbox
      source venv/bin/activate

# while in the sandbox pip install the env for hidden files ( for passwords and API keys)
      pip install  python-dotenv

* to hide the filee use keywords in the python script 

       import os
      from dotenv omport_dotenv

  # load varibales from .env files 

        load_dotenv 

      
