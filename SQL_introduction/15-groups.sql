-- list the number of records grouped by score, ordered by number of records descending

SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
