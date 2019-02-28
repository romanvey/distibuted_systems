MATCH (:Item {id: 3})-[:IN]->()<-[:BUYS]-(persons) RETURN persons
