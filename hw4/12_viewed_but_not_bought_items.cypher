MATCH (:Person {id: 2})-[:VIEWS]->(viewedItems)
MATCH (:Person {id: 2})-[:BUYS]->(orders)
WHERE NOT (orders)<-[:IN]-(viewedItems)
RETURN viewedItems
