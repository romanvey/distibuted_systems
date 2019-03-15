SELECT customer, time, items_list, price, WRITETIME(price) AS write_time FROM orders;
