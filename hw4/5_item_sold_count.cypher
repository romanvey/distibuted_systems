MATCH (item:Item)-[:IN]->(order:Order) WITH item.name AS itemName, COUNT(order) AS timesBought
RETURN itemName, timesBought
