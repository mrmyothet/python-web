-- Database: canteen_automation

-- DROP DATABASE IF EXISTS canteen_automation;

CREATE DATABASE canteen_automation
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'C'
    LC_CTYPE = 'C'
    LOCALE_PROVIDER = 'libc'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;


-- Create Tables 
use canteen_automation;

CREATE TABLE roles (
role_id SERIAL PRIMARY KEY NOT NULL,
role_name VARCHAR(10) NOT NULL
);

CREATE TABLE users(
user_id SERIAL PRIMARY KEY, 
role_id int REFERENCES roles(role_id) ON DELETE SET NULL, 
username varchar(50) NOT NULL,
password varchar(100), 
full_name varchar(100),
email varchar(100), 
contact_number varchar(15), 
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE menu_items(
item_id SERIAL PRIMARY KEY,
item_name VARCHAR(100) NOT NULL, 
description TEXT,
price DECIMAL(10,2) NOT NULL, 
available BOOLEAN DEFAULT TRUE
);

CREATE TABLE inventory (
inventory_id SERIAL PRIMARY KEY,
item_id INT REFERENCES menu_items(item_id) ON DELETE CASCADE, 
stock INT DEFAULT 0,
restock_level INT DEFAULT 10,
last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE orders(
order_id SERIAL PRIMARY KEY, 
user_id INT REFERENCES users(user_id) ON DELETE SET NULL, 
status VARCHAR(50) DEFAULT 'Pending', 
total_amount DECIMAL(10,2),
order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP 
);

CREATE TABLE order_items (
    order_item_id SERIAL PRIMARY KEY,
    order_id INT REFERENCES orders(order_id) ON DELETE CASCADE,
    item_id INT REFERENCES menu_items(item_id) ON DELETE CASCADE,
    quantity INT NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    subtotal DECIMAL(10, 2) GENERATED ALWAYS AS (quantity * price) STORED
);

CREATE TABLE payments (
    payment_id SERIAL PRIMARY KEY,
    order_id INT REFERENCES orders(order_id) ON DELETE SET NULL,
    amount DECIMAL(10, 2) NOT NULL,
    payment_method VARCHAR(50), -- e.g., Credit Card, Cash, Digital Wallet
    payment_status VARCHAR(50) DEFAULT 'Pending', -- e.g., Pending, Completed, Failed
    payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE notifications (
    notification_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(user_id) ON DELETE CASCADE,
    message TEXT NOT NULL,
    status VARCHAR(20) DEFAULT 'Unread',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert data

INSERT INTO roles (role_name)
values
('Admin'), 
('User');

INSERT INTO users (role_id,username,password,full_name,email,contact_number) 
VALUES 
(1,'admin1','password123','Admin One','admin1@test.com','12345'),
(2,'user1','password456','User One','user1@test.com','1232345');

INSERT INTO inventory (item_id, stock, restock_level)
VALUES 
(1, 4, 10),
(2, 30, 5), 
(3, 40, 9)

INSERT INTO orders (user_id, status, total_amount)
VALUES 
(2, 'Pending', 16.97)

INSERT INTO payments(order_id, amount, payment_method, payment_status)
VALUES 
(1, 16.97, 'Credit Card', 'Completed')