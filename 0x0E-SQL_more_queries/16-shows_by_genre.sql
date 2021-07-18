-- FULL OUTER (NOW LEFT JOIN) JOIN + INNER JOIN between 3 tables many to many
SELECT title, name  FROM tv_shows LEFT JOIN
(tv_show_genres INNER JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id)
ON tv_shows.id = show_id
ORDER BY title ASC, name ASC;
