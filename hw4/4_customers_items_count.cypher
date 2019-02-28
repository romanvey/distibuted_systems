MATCH (Person{name:"Andrii"})-[:BUYS]->()<-[:IN]-(items) RETURN count(items)
