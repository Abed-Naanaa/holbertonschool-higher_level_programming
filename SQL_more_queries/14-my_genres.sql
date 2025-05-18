-- Lists genres and the number of shows linked to each genre
SELECT
  genres.name,
  COUNT(tv_show_genres.tv_show_id) AS show_count
FROM genres
LEFT JOIN tv_show_genres ON genres.id = tv_show_genres.genre_id
GROUP BY genres.name
ORDER BY genres.name;
