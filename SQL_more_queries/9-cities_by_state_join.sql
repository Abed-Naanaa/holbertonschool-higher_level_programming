-- Lists all cities with their state names sorted by cities.id in one SELECT statement using JOIN
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
