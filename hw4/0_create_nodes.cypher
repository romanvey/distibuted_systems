CREATE 
(andrii:Person {name:"Andrii", id:1}),
(roman:Person {name:"Roman", id:2}),

(iphone:Item {name:"iPhone 6", price:800, id:1}),
(samsung:Item {name:"Samsung S3", price:600, id:2}),
(cover:Item {name:"cover", price:50, id:3}),
(charger:Item {name:"charger", price:100, id:4}),

(order1:Order {name:"order 1", id:1, price:850}),
(order2:Order {name:"order 2", id:2, price:650}),
(order3:Order {name:"order 3", id:3, price:100}),

(iphone)-[:IN]->(order1),
(cover)-[:IN]->(order1),
(samsung)-[:IN]->(order2),
(cover)-[:IN]->(order2),
(charger)-[:IN]->(order3),

(roman)-[:VIEWS]->(samsung),
(roman)-[:VIEWS]->(iphone),
(roman)-[:VIEWS]->(charger),
(andrii)-[:VIEWS]->(samsung),

(andrii)-[:BUYS]->(order1),
(roman)-[:BUYS]->(order2),
(andrii)-[:BUYS]->(order3)
RETURN *



