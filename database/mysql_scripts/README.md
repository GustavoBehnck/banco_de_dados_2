# Script to drop, create and populate grao_mestre_db database

# Requirements to use this script
1. All of the following script files must be in the same directory;
    a. create.sql
	b. populate.sql
	c. each_row_count.sql
	d. rebuild_db.sh
2. You must have a .my.cnf file in your home directory (~/)
	a. Example can be found in the file /config/.my.cnf

# Suggestion to make it easier
Create a function in your bashrc to run this script passing the first argument
	a. An example can be found in the file /config/bashrc_function.bash
