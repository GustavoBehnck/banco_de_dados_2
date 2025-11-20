# Script to drop, create and populate grao_mestre database

# Requirements to use this script
# 1. All of the following script files must be in the same directory;
#	a. create.sql
#	b. populate.sql
#	c. each_row_count.sql
#	d. rebuild_db.sh
# 2. You must have a .my.cnf file in your home directory (~/)
#	a. Example can be found at example/example.my.cnf

# Suggestion to make it easier
# Create a function in your bashrc to run this script passing the first argument
# 	a. Example can be found at example/bashrc_complement.bash

base_dir_path="$1"
action="$2"

case $action in
	d)
		echo "Dropping database..."
		mariadb -e "DROP DATABASE library_db;"
		echo "Showing result..."
		mariadb -e "SHOW DATABASES;"
		;;
	c)
		echo "Creating database..."
		mariadb < "$base_dir_path/create.sql"
		echo "Showing result..."
		mariadb library_db -e "SHOW TABLES;"
		;;
	p)
		echo "Populating database..."
		mariadb library_db < "$base_dir_path/populate.sql"
		echo "Showing result..."
		mariadb library_db -e "SELECT * from returns;"
		;;
	count)
		echo "Counting rows of each table..."
		mariadb library_db -N -e "
			SELECT GROUP_CONCAT(query SEPARATOR ' UNION ALL ')
			FROM (
				SELECT 
				    CONCAT('SELECT \"', table_name, '\" AS table_name, COUNT(*) AS registers FROM \`', table_schema, '\`.\`', table_name, '\`') AS query
				FROM information_schema.tables
				WHERE table_schema = 'library_db'
			) AS queries;
		" | mariadb library_db | column -t | awk 'BEGIN{c1="\033[37m";c2="\033[36m";r="\033[0m"}{print ((NR%2==0)?c1:c2) $0 r}'
		;;
	*)
		echo "???????"
		return 1
		;;
esac
