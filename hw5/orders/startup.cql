USE shop;

CREATE TABLE orders ( 
customer text,
time Timestamp,
price int,
items_list list<text>,
PRIMARY KEY(customer, time));

INSERT INTO orders (customer, time, price, items_list) 
VALUES ('Roma', '2016-12-15', 600, ['iPhone 6']);

INSERT INTO orders (customer, time, price, items_list) 
VALUES ('Roma', '2016-12-14', 700, ['Galaxy Watch', 'iWatch']);

INSERT INTO orders (customer, time, price, items_list) 
VALUES ('Andrii', '2016-12-15', 600, ['iPhone 6']);

INSERT INTO orders (customer, time, price, items_list) 
VALUES ('Andrii', '2016-11-13', 500, ['iPhone 5']);

INSERT INTO orders (customer, time, price, items_list) 
VALUES ('Andrii', '2016-12-10', 1400, ['SmartTV 2', 'iWatch']);
