# Add this function to your bashrc
gmdb() {
    local base_dir_path="/home/mateus/univap_projects/banco_de_dados_2"
    local final_dir_path="$base_dir_path/database/mysql_scripts"
    "$final_dir_path/rebuild_db.sh" "$final_dir_path" "$1"
}

