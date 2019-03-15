CREATE MATERIALIZED VIEW items_by_name 
AS SELECT * 
FROM items 
WHERE name IS NOT NULL AND category IS NOT NULL AND price IS NOT NULL 
PRIMARY KEY (name, category, price);

SELECT * FROM items_by_name WHERE name='iPhone 6' AND category='Phone';
