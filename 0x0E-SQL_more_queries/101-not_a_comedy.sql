-- lists all shows without the genre Comedy in the
-- database hbtn_0d_tvshows
SELECT title FROM tv_shows LEFT JOIN
(SELECT show_id FROM tv_show_genres INNER JOIN tv_genres
ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_genres.name = "Comedy") AS filter
ON tv_shows.id = show_id WHERE show_id IS NULL
ORDER BY title ASC;
