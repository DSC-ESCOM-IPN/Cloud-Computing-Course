echo "Updating system..."
sudo apt-get update

echo "Instaling apache server and php lang..."
sudo apt-get install apache2 php libapache2-mod-php -y 

echo "Installing MariaDB server and php utils..."
sudo apt-get update
sudo apt-get install mariadb-server php php-mysql -y
