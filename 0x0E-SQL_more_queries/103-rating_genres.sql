-- lists all genres in the database hbtn_0d_tvshows_rate by their rating
SELECT name, SUM(rate) AS rating FROM tv_genres LEFT JOIN
(tv_show_genres INNER JOIN
(tv_shows LEFT JOIN tv_show_ratings ON tv_shows.id = tv_show_ratings.show_id)
ON tv_show_genres.show_id = tv_show_ratings.show_id)
ON tv_genres.id = tv_show_genres.genre_id
GROUP BY name ORDER BY rating DESC;
