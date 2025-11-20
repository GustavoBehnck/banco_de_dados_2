base_dir_path="$1"
action="$2"

case $action in
	d)
		echo "Dropping database..."
		mariadb -e "DROP DATABASE grao_mestre_db;"
		echo "Showing result..."
		mariadb -e "SHOW DATABASES;"
		;;
	c)
		echo "Creating database..."
		mariadb < "$base_dir_path/create.sql"
		echo "Showing result..."
		mariadb grao_mestre_db -e "SHOW TABLES;"
		;;
	p)
		echo "Populating database..."
		mariadb grao_mestre_db < "$base_dir_path/populate.sql"
		echo "Showing result..."
		mariadb grao_mestre_db -e "SELECT * from returns;"
		;;
	count)
		echo "Counting rows of each table..."
		mariadb grao_mestre_db -N -e "
			SELECT GROUP_CONCAT(query SEPARATOR ' UNION ALL ')
			FROM (
				SELECT 
				    CONCAT('SELECT \"', table_name, '\" AS table_name, COUNT(*) AS registers FROM \`', table_schema, '\`.\`', table_name, '\`') AS query
				FROM information_schema.tables
				WHERE table_schema = 'grao_mestre_db'
			) AS queries;
		" | mariadb grao_mestre_db | column -t | awk 'BEGIN{c1="\033[37m";c2="\033[36m";r="\033[0m"}{print ((NR%2==0)?c1:c2) $0 r}'
		;;
	*)
		echo "???????"
		return 1
		;;
esac
