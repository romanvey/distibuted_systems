SELECT customer, max(price) as max_order FROM orders GROUP BY customer;
