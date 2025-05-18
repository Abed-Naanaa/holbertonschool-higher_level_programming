-- Lists shows without any genre linked, showing title and NULL for genre_id
SELECT tv_shows.title, NULL AS genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title ASC;
