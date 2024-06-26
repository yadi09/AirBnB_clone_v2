-- a script that prepares a MySQL server for the project:

CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'Hbnb_test_pwd_09';

GRANT ALL ON hbnb_test_db.* TO hbnb_test@localhost;

GRANT SELECT ON performance_schema.* TO hbnb_test@localhost;
