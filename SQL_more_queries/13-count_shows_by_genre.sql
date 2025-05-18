-- Lists all shows and the number of genres linked to each show
SELECT
  tv_shows.title,
  COUNT(tv_show_genres.genre_id) AS genre_count
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
GROUP BY tv_shows.title
ORDER BY tv_shows.title;
