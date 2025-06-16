-- SELECT title, rental_duration
-- FROM film
-- WHERE title LIKE '%Speed%';

-- % - любое кол-во любых символов
-- _ - 1 любой символ

-- SELECT first_name, email FROM customer
-- WHERE email IS NOT NULL;


-- SELECT first_name, last_name, email FROM customer
-- ORDER BY first_name ASC, last_name DESC
-- OFFSET 20 LIMIT 10;


-- SELECT title AS "Заголовок", rental_duration, rating
-- FROM film
-- WHERE NOT (rating = 'G' OR rating = 'PG') AND rental_duration < 4  AND title LIKE '%on%'
-- ORDER BY title
-- OFFSET 5 LIMIT 10;


SELECT title, rental_duration, rating
FROM film
WHERE NOT (rating = 'G' OR rating = 'PG') AND rental_duration < 4  AND title LIKE '%on%'
ORDER BY title
OFFSET 5 LIMIT 10;