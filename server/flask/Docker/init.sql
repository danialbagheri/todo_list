-- CREATE DATABASE IF NOT EXISTS todoapp;
GRANT ALL PRIVILEGES ON linco.* TO 'todoapp'@'%' IDENTIFIED BY 'secret';
-- CREATE TABLE [IF NOT EXISTS] todoapp.User;
-- CREATE TABLE [IF NOT EXISTS] todoapp.todo;
FLUSH PRIVILEGES;