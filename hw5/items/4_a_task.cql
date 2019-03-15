CREATE INDEX options_keys_ind ON items (KEYS(options));
SELECT * FROM items WHERE options CONTAINS KEY 'color';
