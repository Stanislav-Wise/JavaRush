-- SELECT *
-- FROM rental
-- INNER JOIN customer ON rental.customer_id = customer.customer_id
-- WHERE first_name LIKE 'A%';


-- SELECT customer.first_name, customer.last_name, rental.rental_date
-- FROM rental
-- JOIN customer ON rental.customer_id = customer.customer_id
-- WHERE first_name LIKE 'A%'
-- ORDER BY first_name;


-- SELECT c.first_name, c.last_name, r.rental_date
-- FROM rental r
-- JOIN customer c ON r.customer_id = c.customer_id
-- WHERE c.first_name LIKE 'A%'
-- ORDER BY c.first_name;

-- SELECT c.customer_id, c.first_name, c.last_name, r.rental_date, r.rental_id

-- SELECT *
-- FROM customer c
-- LEFT JOIN rental r ON r.customer_id = c.customer_id
-- WHERE r.rental_date IS NULL
-- ORDER BY c.first_name;


-- SELECT *
-- FROM customer c
-- RIGHT JOIN rental r ON r.customer_id = c.customer_id
-- ORDER BY c.first_name;


-- SELECT *
-- FROM customer c
-- FULL OUTER JOIN rental r ON r.customer_id = c.customer_id
-- ORDER BY c.first_name;


SELECT c.first_name, c.last_name, r.rental_date, f.title
FROM rental r
JOIN customer c ON r.customer_id = c.customer_id
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film f ON f.film_id = i.film_id
ORDER BY c.first_name
LIMIT 100;


