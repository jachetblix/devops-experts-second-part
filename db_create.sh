#!/bin/sh




mysql -u root -e "CREATE DATABASE IF NOT EXISTS $MYSQL_DATABASE;"
# Create tables
mysql -u root -p$MYSQL_ROOT_PASSWORD $MYSQL_DATABASE <<EOF
CREATE TABLE IF NOT EXISTS users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    user_name VARCHAR(255) NOT NULL,
    creation_date INT NOT NULL
);
EOF

# Insert data into tables
mysql -u root -p$MYSQL_ROOT_PASSWORD $MYSQL_DATABASE <<EOF
INSERT INTO users (user_name, creation_date)
VALUES
    ('John Doe', 12.01.1993),
    ('Jane Smith', 15.02.2021),
    ('Bob Johnson', 21.03.2022),
    ('John Doe', 12.01.1995),
    ('Jane Smith', 15.02.2023),
    ('Bob Johnson', 22.04.2020),
    ('John Doe', 12.01.2005),
    ('Jane Smith', 15.02.2007),
    ('Bob Johnson', 21.03.2008);

EOF
mysql -u root -p $MYSQL_ROOT_PASSWORD  -e "ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '$MYSQL_ROOT_PASSWORD';"
echo "Database and tables created and populated successfully!"