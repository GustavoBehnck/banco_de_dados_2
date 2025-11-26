base_dir_path='/home/mateus/univap_projects/banco_de_dados_2/database/mysql_scripts/populate'

mariadb grao_mestre_db < "$base_dir_path/populate_clients.sql"
mariadb grao_mestre_db < "$base_dir_path/populate_farm_addresses.sql"
mariadb grao_mestre_db < "$base_dir_path/populate_farms.sql"
mariadb grao_mestre_db < "$base_dir_path/populate_models.sql"
mariadb grao_mestre_db < "$base_dir_path/populate_vehicles.sql"
mariadb grao_mestre_db < "$base_dir_path/populate_contracts.sql"
mariadb grao_mestre_db < "$base_dir_path/populate_vehicles_contracts.sql"
