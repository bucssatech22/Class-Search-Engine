CREATE DATABASE IF NOT EXISTS test_1;
USE test_1;

CREATE TABLE IF NOT EXISTS courses_db (
    name VARCHAR(255),
    code VARCHAR(100) PRIMARY KEY,
    description TEXT,
    credit FLOAT,
    prereq TEXT,
    hub TEXT
);