CREATE KEYSPACE IF NOT EXISTS shop 
WITH REPLICATION = { 'class' : 'NetworkTopologyStrategy', 'datacenter1' : 1 };

USE shop;


CREATE TABLE items (  
category text,  
name text,  
price int,  
producer text,
options map<text,text>,
PRIMARY KEY (category, price)  
);


INSERT INTO items (category, name, producer, price, options) 
   VALUES ('Phone', 'iPhone 6', 'Apple', 600, {'color': 'grey'});
INSERT INTO items (category, name, producer, price, options) 
   VALUES ('Phone', 'iPhone 5', 'Apple', 500, {'color': 'black'});
INSERT INTO items (category, name, producer, price, options) 
   VALUES ('Phone', 'iPhone 4', 'Apple', 400, {'color': 'grey'});

INSERT INTO items (category, name, producer, price, options) 
   VALUES ('Phone', 'Galaxy S3', 'Samsung', 200, {'color': 'white'});
INSERT INTO items (category, name, producer, price, options) 
   VALUES ('Phone', 'Galaxy S4', 'Samsung', 400, {'color': 'black'});

INSERT INTO items (category, name, producer, price, options) 
   VALUES ('TV', 'SmartTV 2', 'Samsung', 1000, {'diagonal': '40'});
INSERT INTO items (category, name, producer, price, options) 
   VALUES ('TV', 'SmartTV', 'Samsung', 900, {'diagonal': '38'});

INSERT INTO items (category, name, producer, price, options) 
   VALUES ('Smart Watch', 'Galaxy Watch', 'Samsung', 300, {'color': 'black', 'strap':'leather'});
INSERT INTO items (category, name, producer, price, options) 
   VALUES ('Smart Watch', 'iWatch', 'Apple', 400, {'color': 'white', 'strap':'leather'});
