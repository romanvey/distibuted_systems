MATCH (item:Item)-[:IN]->(order:Order) WITH item.name as itemName, COUNT(order) as timesBought
RETURN itemName, timesBought
