MATCH (:Person {id:2})-[:VIEWS]->(items:Item), (:Person {id:2})-[:BUYS]->(roman_orders)
WHERE NOT (roman_orders)<-[:IN]-(items) RETURN items
