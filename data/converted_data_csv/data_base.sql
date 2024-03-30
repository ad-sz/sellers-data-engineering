CREATE DATABASE data_base;
use data_base

CREATE TABLE inventory_status (
    id_product INT,
    quantity_in_stock INT,
    pallet_space VARCHAR(50),
    posting_date DATE
);

CREATE TABLE products (
    id_product INT,
    category_product VARCHAR(100),
    name_product VARCHAR(100),
    unit_price DECIMAL(10, 2)
);

CREATE TABLE sales_transactions (
    id_transaction VARCHAR(50),
    name_customer VARCHAR(100),
    name_product VARCHAR(100),
    quantity_sold INT,
    region VARCHAR(100),
    id_seller VARCHAR(50)
);

CREATE TABLE sellers (
    id_seller VARCHAR(50),
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    employment_date DATE,
    date_of_birth DATE,
    region VARCHAR(100)
);

CREATE TABLE customers (
    id_customer VARCHAR(50),
    name_customer VARCHAR(100),
    date_added_customer DATE,
    region VARCHAR(100),
    id_seller VARCHAR(50)
);

SELECT * FROM customers;

TRUNCATE TABLE customers;
TRUNCATE TABLE inventory_status;
TRUNCATE TABLE products;
TRUNCATE TABLE sales_transactions;
TRUNCATE TABLE sellers;
