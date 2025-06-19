SELECT
	title,
	length,
	CASE
		WHEN length > 120 THEN 'Длинный'
		WHEN length < 60 THEN 'Короткий'
		ELSE 'Обычный'
	END AS film_type
FROM film;