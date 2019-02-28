// Add "cover" item purchase, so now it bought two times 

MATCH 
(roman:Person{name:"Roman"}), 
(andrii:Person{name:"Andrii"}), 
(i:Item{name:"cover"}),
CREATE 
(order4:Order{name:"order 4", price:50, id:4}),
(order5:Order{name:"order 5", price:50, id:5}),
(order6:Order{name:"order 6", price:50, id:6}),
(roman)-[:BUYS]->(order4),
(andrii)-[:BUYS]->(order5),
(andrii)-[:BUYS]->(order6),
(order4)<-[:IN]-(i),
(order5)<-[:IN]-(i),
(order6)<-[:IN]-(i)
RETURN *

// Now lets found all items bought more than 1 time
// (it would be "cover" item)

MATCH (:Person{ name: "Roman"})-[:BUYS]->(orders)<-[:IN]-(items)
WITH items.name AS itemName, COUNT(orders) AS frequency
WHERE frequency >= 2
RETURN itemName, frequency
ORDER BY frequency DESC

MATCH (:Person{ name: "Andrii"})-[:BUYS]->(orders)<-[:IN]-(items)
WITH items.name AS itemName, COUNT(orders) AS frequency
WHERE frequency >= 2
RETURN itemName, frequency
ORDER BY frequency DESC

// Now this code can find the most sellable items for specific customer
