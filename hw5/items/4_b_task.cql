CREATE INDEX options_ind ON items (ENTRIES(options));
SELECT * FROM items WHERE options['diagonal']='38';
