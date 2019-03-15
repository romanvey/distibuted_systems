CREATE INDEX producer_ind ON items (producer);
SELECT * FROM items WHERE category='Phone' AND producer='Apple';
