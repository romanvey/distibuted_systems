SELECT customer, sum(price) as total_price FROM orders GROUP BY customer;
