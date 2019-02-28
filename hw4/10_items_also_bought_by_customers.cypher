MATCH (:Item {id: 3})-[:IN]->(orders)<-[:BUYS]-(persons)
MATCH (persons)-[:BUYS]->(orders)<-[:IN]-(items) RETURN items
