-- SELECT DISTINCT city_id FROM address;

-- SELECT DISTINCT city_id, district FROM address;

-- SELECT customer_id, COUNT(*) AS num_payments, AVG(amount) AS avg_amount
-- FROM payment
-- GROUP BY customer_id
-- HAVING AVG(amount) > 3
-- ORDER BY avg_amount;

-- SELECT customer_id
-- FROM payment
-- ORDER BY customer_id;


-- SELECT *
-- FROM category cat
-- JOIN film_category fc ON cat.category_id = fc.category.id;

-- SELECT * FROM film_category fc;

SELECT c.name, COUNT(f.film_id) AS num_films FROM category c
JOIN film_category fc ON c.category_id = fc.category_id
JOIN film f ON fc.film_id = f.film_id
GROUP BY c.name
HAVING COUNT(f.film_id) > 50
ORDER BY num_films DESC;