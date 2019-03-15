BEGIN BATCH
UPDATE orders SET items_list = items_list + ['SmartTV 2'] WHERE customer = 'Roma' AND time = '2016-12-15';
UPDATE orders SET price = 1600 WHERE customer = 'Roma' AND time = '2016-12-15';
APPLY BATCH;
// For visualization purposes
SELECT * FROM orders;
