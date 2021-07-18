-- INNER JOIN 3 tables many to many
SELECT tv_genres.name AS name FROM tv_shows INNER JOIN
(tv_show_genres INNER JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id)
ON tv_shows.id = tv_show_genres.show_id WHERE tv_shows.title = "Dexter"
ORDER BY name ASC;
