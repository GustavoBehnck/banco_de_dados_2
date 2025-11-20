# Add this function to your bashrc
gmdb() {
    local base_dir_path="/home/mateus/univap_projects/banco_de_dados2"
    "$base_dir_path/database/scripts/rebuild_db.sh" "$base_dir_path" "$1"
}
