MATCH (:Item {id: 1})<-[:VIEWS]-(persons)
MATCH (persons)-[:BUYS]->(orders)<-[:IN]-(items) RETURN items
