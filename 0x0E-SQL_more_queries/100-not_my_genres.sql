-- uses the hbtn_0d_tvshows database to list all genres
-- not linked to the show Dexter
SELECT name FROM tv_genres LEFT JOIN
(SELECT genre_id FROM tv_show_genres INNER JOIN tv_shows
ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = "Dexter") AS filter
ON tv_genres.id = filter.genre_id WHERE filter.genre_id IS NULL
GROUP BY name ORDER BY name ASC;
