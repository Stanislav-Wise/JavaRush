-- SELECT first_name AS "Имя", last_name as Фамилия FROM actor;

-- SELECT FIRST_NAME, EMAIL FROM STAFF;

-- SELECT столбцы
-- FROM таблица
-- WHERE условия;

-- SELECT *
-- FROM customer
-- WHERE first_name = 'Lisa';


-- SELECT *
-- FROM customer
-- WHERE store_id != 1;


-- SELECT first_name AS "Имя"
-- FROM customer
-- WHERE store_id < 2;

-- SELECT *
-- FROM customer
-- WHERE first_name > 'L';



-- SELECT *
-- FROM customer
-- WHERE first_name > 'L' AND  (store_id = 1 OR last_name > 'S');


-- SELECT *
-- FROM customer
-- WHERE  NOT store_id = 1;


-- SELECT *
-- FROM film
-- -- WHERE rating = 'R' OR rating = 'G';
-- WHERE rating NOT IN ('R', 'G') AND rental_duration >= 5;


-- SELECT title, rental_duration
-- FROM film
-- WHERE rental_duration >= 5 AND rental_duration <= 6;

SELECT title, rental_duration
FROM film
WHERE rental_duration BETWEEN 6 AND 7;