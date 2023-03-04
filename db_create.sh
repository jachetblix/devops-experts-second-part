#!/bin/sh
echo 'Creating user'
mysql -u $MYSQL_ROOT_USER -p$MYSQL_ROOT_PASSWORD -e "CREATE USER IF NOT EXISTS $MYSQL_USER@$MYSQL_HOST IDENTIFIED WITH mysql_native_password BY '$MYSQL_PASSWORD';"
mysql -u $MYSQL_ROOT_USER -p$MYSQL_ROOT_PASSWORD -e "ALTER USER IF EXISTS $MYSQL_USER@$MYSQL_HOST IDENTIFIED WITH mysql_native_password BY '$MYSQL_PASSWORD';"

echo 'create database'
mysql -u $MYSQL_ROOT_USER -p$MYSQL_ROOT_PASSWORD -e "CREATE DATABASE IF NOT EXISTS $MYSQL_DATABASE;"
# Create tables
echo 'creating users table'
mysql -u $MYSQL_ROOT_USER -p$MYSQL_ROOT_PASSWORD $MYSQL_DATABASE <<EOF
CREATE TABLE IF NOT EXISTS users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    user_name VARCHAR(255) NOT NULL
);
EOF
echo 'filling users table'
# Insert data into tables
mysql -u $MYSQL_ROOT_USER -p$MYSQL_ROOT_PASSWORD $MYSQL_DATABASE <<EOF
INSERT INTO users (user_name)
VALUES
    ('John Doe'),
    ('Jane Smith'),
    ('Bob Johnson'),
    ('John Folk'),
    ('Jane Smoozy'),
    ('Bob Derosk'),
    ('John Boby'),
    ('John Nolan'),
    ('Jane Smooth'),
    ('Bob Kools');

EOF
mysql -u $MYSQL_ROOT_USER -p$MYSQL_ROOT_PASSWORD $MYSQL_DATABASE -e "GRANT ALL PRIVILEGES ON $MYSQL_DATABASE.* TO $MYSQL_USER@$MYSQL_HOST;"
echo "Database and tables created and populated successfully!"