INSERT INTO orders (customer, time, price, items_list) 
VALUES ('Roma', '2016-12-18', 1000, ['SmartTV 2']) USING TTL 5;

// For visualization purposes
SELECT * FROM orders;
// Wait 5 seconds
SELECT * FROM orders;
