CREATE INDEX items_ind ON orders (items_list);
SELECT * FROM orders WHERE customer='Roma' AND items_list CONTAINS 'iWatch';

