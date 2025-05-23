-- Lists cities in California sorted by cities.id without using JOIN
SELECT id, name
FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id ASC;
